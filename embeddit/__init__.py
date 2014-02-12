from embeddit.routing import RegexConverter
from flask import Flask
from flask.ext.assets import Environment, Bundle
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.url_map.converters['regex'] = RegexConverter
app.url_map.redirect_defaults = False
app.url_map.strict_slashes = False

# Setup Flask-Assets
assets = Environment(app)

# JS Library Bundle
js_lib = Bundle(
    'lib/iframeResizer.contentWindow.min.js',
    'lib/jquery-2.1.0.min.js',
    'lib/moment.min.js',
    'lib/livestamp.min.js',

    filters='jsmin',
    output='gen/js_lib.js'
)
assets.register('js_lib', js_lib)

# JS Comment + Link bundle
js_cl = Bundle(
    'js/comment.js',
    'js/link.js',

    filters='jsmin',
    output='gen/js_cl.js'
)
assets.register('js_cl', js_cl)

# JS Link Bundle
js_l = Bundle(
    'js/link.js',

    filters='jsmin',
    output='gen/js_l.js'
)
assets.register('js_l', js_l)

# CSS Comment + Link bundle
css_cl = Bundle(
    'css/global.css',
    'css/link.css',
    'css/comment.css',

    filters='cssmin',
    output='gen/css_cl.css'
)
assets.register('css_cl', css_cl)

# CSS Link Bundle
css_l = Bundle(
    'css/global.css',
    'css/link.css',

    filters='cssmin',
    output='gen/css_l.css'
)
assets.register('css_l', css_l)

# CSS Subreddit Bundle
css_s = Bundle(
    'css/global.css',
    'css/subreddit.css',

    filters='cssmin',
    output='gen/css_s.css'
)
assets.register('css_s', css_s)

import views
