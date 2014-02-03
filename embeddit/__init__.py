from flask import Flask
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

import views
