import io
import base64
import urllib

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
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
    # global plot_url
    img = io.BytesIO()

    at = pd.read_pickle('../2018_at.pickle.gzip')
    at_sub = at.tail(1000)
    sns.set_style('whitegrid')
    mpl.rcParams['patch.force_edgecolor'] = True

    sns.set(rc={'figure.figsize':(5.0, 5.0)})
    p1 = sns.countplot(x='Group', data=at_sub, palette='coolwarm')
    p1.set_xticklabels(p1.get_xticklabels(), rotation=90);

    # avoid xticklabels cut off
    p1.figure.tight_layout()
    p1.figure.savefig(img, format='png')
    p1.figure.savefig('p1.png')
    img.seek(0)

    # base64 encode & URL-escape
    plot_url = urllib.parse.quote(base64.b64encode(img.read()).decode())
    # plot_url = base64.b64encode(img.getvalue())

    return render_template('plot.html', title='Plot', plot_url=plot_url) 
    # return '<img src="data:image/png;base64,{}">'.format(plot_url)


if __name__ == '__main__':
    initialize()
    app.run(debug=True)

