from flask.ext.assets import Bundle

css = Bundle(
    'css/lib/bootstrap/css/bootstrap.min.css',
    'css/src/base.css',    
    filters=['cssrewrite'],
    output='gen/css/base.css'
)