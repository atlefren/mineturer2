from flask.ext.assets import Bundle

js_filters = []
css_filters = []


#if not app.debug:
# Use jsmin and cssmin when not running in debug
#js_filters.append('jsmin')
css_filters.append('cssmin')

base_css = Bundle(
    'css/lib/bootstrap/css/bootstrap.min.css',
    Bundle (
        'css/src/base.css',    
        filters=css_filters,
    ),    
    filters=['cssrewrite'],
    output='gen/css/base.css'
)

login = Bundle(    
    base_css,
    Bundle (
        'css/src/login.css',    
        filters=css_filters,
    ),    
    filters=['cssrewrite'],
    output='gen/css/login.css'
)

base_js = Bundle(
    'js/lib/jquery-1.11.1.min.js',
    'js/lib/bootstrap.min.js',     
    output='gen/js/libs.js'
)

triplist_css = Bundle(
    base_css,
    Bundle (
        'css/lib/leaflet-0.7.3/leaflet.css',
        filters=css_filters,
    ),
    filters=['cssrewrite'],
    output='gen/js/triplist.css'
)

triplist_js = Bundle(
    base_js,
    'js/lib/underscore-min.js',
    'js/lib/backbone-min.js',
    'js/lib/leaflet.js',
    'js/lib/SpatialBB.min.js',
    Bundle(
        'js/src/triplist.js',
        filters=js_filters,
    ),
    output='gen/js/triplist_js.js'
)