# -*- coding: utf-8 -*-
import os

from flask import Flask
from webassets.loaders import PythonLoader
from flask.ext.assets import Environment, Bundle

from views import create_views
#from assetbundle import create_bundles

def create_bundles(app):
  assets = Environment(app)
  assets.debug = True if app.debug == 'True' else False
  bundles = PythonLoader('assetbundle').load_bundles()
  for name, bundle in bundles.iteritems():
    assets.register(name, bundle)

def create_app(debug):
  app = Flask(__name__)
  app.debug = debug
  
  create_bundles(app)
  create_views(app)

  return app


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app = create_app(os.environ.get('DEBUG', False))
    app.run(host='0.0.0.0', port=port, debug=True)