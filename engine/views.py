from flask import Blueprint, request, render_template, flash, g, session, \
    redirect, url_for

import config
from engine.forms import InitialForm, EngineSelectForm
from engine.models.engines import Engine
from engine.models.initial_parameters_model import InitialParametersModel

engine = Blueprint('', __name__,
                   template_folder=config._basedir + '/templates')


@engine.before_request
def before_request():
    g.initials = InitialParametersModel()
    if InitialParametersModel.__name__ in session:
        g.initials.load()


@engine.route('/')
def home():
    return render_template("engine/start.html", initials=g.initials)


@engine.route('/initials/', methods=['GET', 'POST'])
def initials():
    """
    Форма ввода начальных данных
    """
    form = InitialForm(request.form, obj=g.initials)
    if form.validate_on_submit():
        initials = InitialParametersModel()
        initials.update(form.data)
        initials.save()
        session['calculated_power'] = initials.calculate_power()
        return redirect(url_for('engine.pre_engine_select'))
    flash('Что-то не так', 'error-message')
    return render_template("engine/initial.html", form=form)


@engine.route('/pre_engine_select/', methods=['GET', 'POST'])
def pre_engine_select():
    """
    Форма выбора двигателя по результатам рассчета
    """
    power = session['calculated_power']
    engines = Engine.select().where(Engine.nominal_power > power)
    form = EngineSelectForm(request.form)
    form.engine = engines
    if form.validate_on_submit():
        return redirect(url_for('engine.home'))
    return render_template("engine/pre_engine_select.html", form=form,
                           engines=engines, power=power)
