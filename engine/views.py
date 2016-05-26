from flask import Blueprint, request, render_template, flash, g, session, \
    redirect, url_for
from playhouse.shortcuts import model_to_dict, dict_to_model

import config
from engine.calculations import Calculations
from engine.forms import InitialForm, EngineSelectForm, EngineForm
from engine.models.base_model import database
from engine.models.engines import Engine
from engine.models.initial_parameters_model import InitialParametersModel

engine = Blueprint('', __name__,
                   template_folder=config._basedir + '/templates')


@engine.before_request
def before_request():
    g.initials = InitialParametersModel()
    g.initials.load(session)

@engine.before_request
def _db_connect():
    database.connect()


@engine.teardown_request
def _db_close(exc):
    if not database.is_closed():
        database.close()


@engine.route('/')
def home():
    return render_template("engine/start.html", initials=g.initials)


@engine.route('/initials/', methods=['POST'])
def initials():
    """
    Форма ввода начальных данных
    """
    form = InitialForm(request.form)

    if form.validate_on_submit():
        form.populate_obj(g.initials)
        g.initials.save(session)
        session['calculated_power'] = Calculations.calculate_power(g.initials)
        return redirect(url_for('.pre_engine_select'))
    else:
        flash('Что-то не так: {}'.format(form.errors), 'error_message')
    return render_template("engine/initial.html", form=form)


@engine.route('/initials/', methods=['GET'])
def initials_get():
    form = InitialForm(request.form, obj=g.initials)
    return render_template("engine/initial.html", form=form)


@engine.route('/pre_engine_select/', methods=['GET', 'POST'])
def pre_engine_select():
    """
    Форма выбора двигателя по результатам рассчета
    """
    power = session.get('calculated_power')
    engines = list(
        Engine.select().where(Engine.nominal_power > power).iterator())
    session['engines'] = [model_to_dict(engine) for engine in engines]
    form = EngineSelectForm(request.form)
    form.engine.choices = {engine.id: engine.name for engine in engines}.items()
    if form.validate_on_submit():
        return redirect(url_for('.final_engine_select'))
    return render_template("engine/pre_engine_select.html", form=form,
                           engines={item.id: item for item in
                                    engines}, power=power)


@engine.route('/add_engine/', methods=['GET', 'POST'])
def add_engine():
    """
    Форма добавления двигателя в список двигателей
    """
    form = EngineForm(request.form)
    if form.validate_on_submit():
        engine = Engine()
        form.populate_obj(engine)
        engine.id = None if engine.id == '' else engine.id
        engine.save()
        return redirect(url_for('.add_engine'))
    return render_template("engine/add_engine.html", form=form,
                           header='Добавление двигателя', button='Добавить')


@engine.route('/edit_engine/', methods=['POST'])
@engine.route('/edit_engine/<int:idx>', methods=['GET'])
def edit_engine(idx=None):
    """
    Форма изменения двигателя
    """
    form = EngineForm()
    if request.method == 'POST':
        form = EngineForm(request.form)
    if request.method == 'GET':
        engine = Engine.get(Engine.id == idx)
        form = EngineForm(request.form, obj=engine)
    if form.validate_on_submit():
        form.populate_obj(engine)
        engine.id = None if engine.id == '' else engine.id
        engine.save()
        return redirect(url_for('.pre_engine_select'))
    return render_template("engine/add_engine.html", form=form,
                           header='Редактирование двигателя', button='Изменить')



@engine.route('/final_engine_select/', methods=['GET', 'POST'])
def final_engine_select():
    """
    Форма выбора двигателя по результатам рассчета
    """
    power = session.get('calculated_power')
    engines = [dict_to_model(Engine, engine) for engine in session.get('engines')]

    for engine in engines:
        prefer = Calculations.check_engine(g.initials, power, engines, engine)

    form = EngineSelectForm(request.form)
    form.engine.choices = {engine.id: engine.name for engine in engines}.items()

    if form.validate_on_submit():
        return redirect(url_for('.home'))

    return render_template("engine/final_engine_select.html", form=form,
                           engines={item.id: item for item in
                                    engines}, power=power)