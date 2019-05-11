from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_material import Material
from flask_moment import Moment

app = Flask(__name__)
Bootstrap(app)
Material(app)
Moment(app)


@app.route('/')
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow())


@app.route('/material')
def index_material():
    return render_template('index-material.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
