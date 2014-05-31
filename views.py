# -*- coding: utf-8 -*-
import json

from flask import (render_template, g, request, current_app, flash, redirect,
                   url_for, abort)
from flask.ext.login import login_required, current_user
from shapely.geometry import mapping

from models import Trip
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

    @app.route('/trips')
    @login_required
    def trips():
        trips = [trip.serialize_with_point() for trip in current_user.trips]
        return render_template('trips.html', trips=json.dumps(trips))

    @app.route('/trips/<int:id>')
    def trip_detail(id):

        trip = current_app.db_session.query(Trip).get(id)
        if not trip:
            abort(404)        
        return render_template(
            'trip_detail.html',
            trip=trip,
            geom=json.dumps(mapping(trip.geom))
        )
