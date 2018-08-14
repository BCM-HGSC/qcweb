# First come standard libraries, in alphabetical order.

# After a blank line, import third-party libraries.
from flask import Flask
from flask import flash
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask_wtf import FlaskForm
from wtforms import (BooleanField, DateField, DateTimeField,
                     RadioField, SelectField, StringField,
                     SubmitField, TextAreaField, TextField)

from wtforms.validators import DataRequired

# After another blank line, import local libraries.
from .selection import head, sub_demo
from .plotting import plot_demo
from .form_fields import QueryForm

# flask knows where to look for static & template files
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route("/")
@app.route("/home")
def home():
    print('hello from /home')
    return render_template('home.html', title='Home')


@app.route("/table")
def table():
    return render_template('table.html', title='Table', data=head())


@app.route("/query", methods=['GET', 'POST'])
def query():
    print('hello from /query')
    # create instance of the form
    form = QueryForm(request.form)
    # if the form is valid on submission
    is_valid = form.validate_on_submit()
    print('validation result', is_valid)
    if is_valid:
        print('It validated')
        # grab the data from the query on the form
        session['qcreport'] = form.qcreport.data
        session['platform'] = form.platform.data
        session['group'] = form.group.data
        session['appl'] = form.appl.data
        session['start'] = form.start.data
        session['end'] = form.end.data
        session['agg'] = form.agg.data
        session['plot_choice'] = form.plot_choice.data
        session['display_table'] = form.display_table.data
        want_table = True  # TODO: make False based on form
        print('results')
        if want_table:
            return redirect(url_for("table"))
        else:
            return redirect(url_for("plot"))
    # assert 0
    print('back to query.html')
    return render_template('query.html', title='Query', form=form)


@app.route("/plot")
def plot():
    return render_template('plot.html', title='Plot')


@app.route("/plots/p1.png")
def p1_png():
    at_sub = sub_demo()
    image_data, image_type = plot_demo(at_sub)
    resp = make_response(image_data)
    resp.content_type = image_type
    return resp
