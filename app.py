import io
import base64
import urllib

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import make_response
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import seaborn as sns


# flask knows where to look for static & template files
app = Flask(__name__)


dummy = [
    {
        'author': 'Jennifer Watt',
        'title': 'Testing',
        'content': 'Just testing...',
        'date': 'July 25, 2018'
    }
]


def initialize():
    global at
    global at_head
    at = pd.read_pickle('../2018_at.pickle.gzip')
    at_head = at.head()


@app.route("/")
@app.route("/home")
def home():
    # by passing in variable tests (1st one), you get the tests in home.html
    # argument tests (2nd one) is equal to the dummy data
    return render_template('home.html', tests=dummy)


@app.route("/table")
def table():
    return render_template('table.html', title='Table', data=at_head)


@app.route('/plot')
def plot():
    return render_template('plot.html', title='Plot')


@app.route('/plots/p1.png')
def p1_png():
    img = io.BytesIO()

    # select number of rows from dataframe
    at_sub = at.iloc[-1000:, :]

    # matplot/ seaborn style setting
    sns.set_style('whitegrid')
    mpl.rcParams['patch.force_edgecolor'] = True
    sns.set(rc={'figure.figsize':(5.0, 5.0)})

    # seaborn countplot
    p1 = sns.countplot(x='Group', data=at_sub, palette='coolwarm')

    # rotate xticklabels to prevent the labels being overlapped
    p1.set_xticklabels(p1.get_xticklabels(), rotation=90);

    # adjust subplot params to avoid axis labels,titles or ticklabels being clipped
    p1.figure.tight_layout()
    p1.figure.savefig(img, format='png')

    # results
    png_data = img.getvalue()
    resp = make_response(png_data)
    resp.content_type = "image/png"
    return resp


if __name__ == '__main__':
    initialize()
    app.run(debug=True)

