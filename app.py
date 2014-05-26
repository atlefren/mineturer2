# -*- coding: utf-8 -*-
import os

from flask import Flask
from webassets.loaders import PythonLoader
from flask.ext.assets import Environment, Bundle

from views import create_views
from database import init_db, Base

def create_bundles(app):
  assets = Environment(app)
  assets.debug = True if app.debug == 'True' else False
  bundles = PythonLoader('assetbundle').load_bundles()
  for name, bundle in bundles.iteritems():
    assets.register(name, bundle)

def create_app(debug, database_url):
  app = Flask(__name__)
  app.secret_key = os.environ.get('SECRET_KEY', 'development_fallback')
  app.debug = debug
  (app.db_session, app.db_metadata, app.db_engine) = init_db(database_url)

  Base.metadata.create_all(app.db_engine)

  create_bundles(app)
  create_views(app)

  return app


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    db = os.environ.get('BOOKING_DATABASE_URL', 'sqlite:////tmp/mineturer.db')
    app = create_app(os.environ.get('DEBUG', False), db)
    app.run(host='0.0.0.0', port=port, debug=True)