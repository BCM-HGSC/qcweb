# First come standard libraries, in alphabetical order.

# After a blank line, import third-party libraries.
from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import make_response

# After another blank line, import local libraries.
from .selection import head, sub_demo
from .plotting import plot_demo

# flask knows where to look for static & template files
app = Flask(__name__)


@app.route("/")
@app.route("/demo")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')


@app.route("/table")
def table():
    return render_template('table.html', title='Table', data=head())


@app.route("/query")
def query():
    return render_template('query.html', title='Query')


@app.route("/plot")
def plot():
    return render_template('plot.html', title='Plot')


@app.route('/plots/p1.png')
def p1_png():
    at_sub = sub_demo()
    image_data, image_type = plot_demo(at_sub)
    resp = make_response(image_data)
    resp.content_type = image_type
    return resp


@app.route('/demo/plot')
def demo_plot():
    return render_template('demo_plot.html', title='Demo Plot')


@app.route('/demo/plot/p1.png')
def p1_png():
    at_sub = sub_demo()
    image_data, image_type = plot_demo(at_sub)
    resp = make_response(image_data)
    resp.content_type = image_type
    return resp
