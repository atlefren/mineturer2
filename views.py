# -*- coding: utf-8 -*-
import json

from flask import (render_template, g, request, current_app, flash, redirect,
                   url_for)
from flask.ext.login import login_required, current_user


from login_views import create_login_views


def create_views(app):

    create_login_views(app)

    @app.before_request
    def before_request():
        g.user = current_user

    @app.route('/')
    def index():
        if current_user.is_authenticated():
            return redirect(url_for('trips'))
        return render_template('index.html')

    @app.route('/editprofile', methods=['GET', 'POST'])
    def editprofile():
        if request.method == 'GET':
            return render_template(
                'editprofile.html',
                user=current_user,
                errors={},
                edit=True
            )

        if request.form['password'] and request.form['password'] != '':
            current_user.set_password(
                request.form['password'],
                request.form['password2']
            )
        current_user.email = request.form['email'],
        current_user.fullname = request.form['fullname']

        if current_user.validate():
            current_app.db_session.add(current_user)
            current_app.db_session.commit()
            flash('Profilen ble oppdatert!')

        return render_template(
            'editprofile.html',
            errors=current_user.validation_errors,
            user=current_user,
            edit=True
        )

    @app.route('/trips', methods=['GET', 'POST'])
    @login_required
    def trips():
        trips = [trip.serialize() for trip in current_user.trips]
        return render_template('trips.html', trips=json.dumps(trips))
