from flask.ext.assets import Bundle

css = Bundle(
    'css/lib/bootstrap/css/bootstrap.min.css',
    'css/src/base.css',    
    filters=['cssrewrite'],
    output='gen/css/base.css'
)

login = Bundle(    
    'css/src/login.css',    
    filters=['cssrewrite'],
    output='gen/css/login.css'
)

js = Bundle(
    'js/lib/jquery-1.11.1.min.js',
    'js/lib/bootstrap.min.js',
    
    #filters='jsmin',
    output='gen/js/libs.js'
)