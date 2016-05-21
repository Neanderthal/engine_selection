from flask import Blueprint, request, render_template, flash, g, session, \
    redirect, url_for

import config
from engine.forms import InitialForm
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
    Login form
    """
    form = InitialForm(request.form, obj = g.initials)
    # make sure data are valid, but doesn't validate password is right
    if form.validate_on_submit():
        initials = InitialParametersModel()
        initials.update(form.data)
        initials.save()
        return redirect(url_for('engine.step_1'))
    flash('Wrong email or password', 'error-message')
    return render_template("engine/initial.html", form=form)


@engine.route('/step_1/', methods=['GET', 'POST'])
def initial():
    """
    Login form
    """
    form = InitialForm(request.form)
    # make sure data are valid, but doesn't validate password is right
    if form.validate_on_submit():
        # the session can't be modified as it's signed,
        # it's a safe place to store the user id
        return redirect(url_for('engine.home'))
    flash('Wrong email or password', 'error-message')
    return render_template("engine/step_1.html", form=form, initials=g.initials)
