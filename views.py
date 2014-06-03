# -*- coding: utf-8 -*-
import json

from flask import (render_template, g, request, current_app, flash, redirect,
                   url_for, abort)
from flask.ext.login import login_required, current_user
from shapely.geometry import mapping

from models import Trip
from login_views import create_login_views
from filters import create_filters
from parse_gpx import parse_gpx

TRIP_TYPES = {
    'hiking': u'Fjelltur',
    'jogging': u'Joggetur',
    'walking': u'Gåtur',
    'cycling': u'Sykling',
    'nordicski': u'Skitur',
    'car': u'Biltur',
    'swimming': u'Svømmetur',
    'rollerskate': u'Rulleskøyter',
    'snowshoeing': u'Truger',
    'motorbike': u'Motorsykkel',
    'snowmobiling': u'Snøscooter',
    'atv': u'ATV',
    'default': u'Annet',
}


def create_views(app):

    create_filters(app)
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

    ALLOWED_EXTENSIONS = set(['gpx'])

    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    @app.route('/upload', methods=['GET', 'POST'])
    @login_required
    def upload():
        errors = {}
        data = {}
        if request.method == 'POST':

            file = request.files['file']
            title = request.form['title']
            type = request.form['type']
            description = request.form['description']

            if not title or title == '':
                errors['title'] = 'Oppgi en tittel'
            if not file:
                errors['file'] = u'Du må angi en fil.'
            elif not allowed_file(file.filename):
                errors['file'] = u'Ugyldig filtype! (må være en av %s)' % \
                    ', '.join(ALLOWED_EXTENSIONS)
            data['title'] = title
            data['type'] = type
            data['description'] = description
            if not errors:

                points = parse_gpx(file)   
                trip = Trip(
                    user=current_user,
                    title=title,
                    description=description,
                    type=type,
                    start=points[0].time,
                    stop=points[-1].time,
                )
                trip.points = points
                current_app.db_session.add(trip)
                current_app.db_session.commit()
                flash(u'Turen ble lagret!')
                return redirect(url_for('trip_detail', id=trip.id))

        return render_template(
            'upload.html',
            trip_types=TRIP_TYPES,
            errors=errors,
            data=data
        )

    @app.route('/trips/<int:id>')
    def trip_detail(id):

        trip = current_app.db_session.query(Trip).get(id)
        if not trip:
            abort(404)
        return render_template(
            'trip_detail.html',
            trip=trip,
            trip_types=TRIP_TYPES,
            geom=json.dumps(mapping(trip.geom))
        )
