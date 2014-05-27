# -*- coding: utf-8 -*-
import json

from flask import render_template, g
from flask.ext.login import login_required, current_user

from login_views import create_login_views


def create_views(app):

create_login_views(app)

    @app.before_request
    def before_request():
        g.user = current_user

    @app.route('/')
    def index():    
        return render_template('index.html')

    @app.route('/editprofile')
    def editprofile():  
        return render_template('index.html')

    @app.route('/trips', methods=['GET', 'POST'])
    @login_required
    def trips():
        trips = [
        {
            "position": {"lon": 10, "lat": 60},
            "id": 458,
            "type": "nordicski",
            "date": "10. februar 2013",
            "title": "Skitur Klæbu"
        },
        {
            "position": {"lon": 11, "lat": 60},
            "id": 409,
            "type": "jogging",
            "date": "10. oktober 2012",
            "title": "Løpetur 10.10.12"
        },
        {
            "position": {"lon": 11.5, "lat": 60},
                "id": 403,
            "type": "walking",
            "date": "30. september 2012",
            "title": "Søndagstur sept 2012"
        },
        {
            "position": {"lon": 11, "lat": 62},
            "id": 363,
            "type": "hiking",
            "date": "2. september 2012",
            "title": "Skarvan dag 2"
        },
        {
            "position": {"lon": 11, "lat": 59},
            "id": 362,
            "type": "hiking",
            "date": "1. september 2012",
            "title": "Skarvan dag 1"
        },
        {
            "position": {"lon": 11, "lat": 59.5},
            "id": 355,
            "type": "default",
            "date": "25. august 2012",
            "title": "Seladon 25. aug"
        },
        {
            "position": {"lon": 11, "lat": 58},
            "id": 354,
            "type": "default",
            "date": "24. august 2012",
            "title": "Seladon 24 aug"
        },
        {
            "position": {"lon": 9.5, "lat": 58.8},
            "id": 342,
            "type": "hiking",
            "date": "12. august 2012",
            "title": "Øverfjellet-Skarven"
        },
        {
            "position": {"lon": 9.3, "lat": 58.8},
            "id": 341,
            "type": "hiking",
            "date": "11. august 2012",
            "title": "Ruten"
        },
        {
            "position": {"lon": 9.2, "lat": 58.8},
            "id": 327,
            "type": "jogging",
            "date": "31. juli 2012",
            "title": "Joggetur 31.07.12"
        }
        ]


        return render_template('trips.html', trips=json.dumps(trips))