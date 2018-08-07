# First come standard libraries, in alphabetical order.
import io
import base64
import urllib

# After a blank line, import third-party libraries.
from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import make_response
from matplotlib import cm # color
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import seaborn as sns

# After another blank line, import local libraries.


# flask knows where to look for static & template files
app = Flask(__name__)


dummy = [
    {
        'author': 'Jennifer Watt',
        'title': 'All Time',
        'content': 'QC demo for All Time Data',
        'date': 'August 6, 2018'
    }
]


def initialize():
    global df_at
    global df_at_head
    df_at = pd.read_pickle('../data/at.pickle.gzip')
    df_at_head = df_at.head()


@app.route("/")
@app.route("/home")
def home():
    # by passing in variable tests (1st one), you get the tests in home.html
    # argument tests (2nd one) is equal to the dummy data
    return render_template('home.html', tests=dummy)


@app.route("/table")
def table():
    return render_template('table.html', title='Table', data=df_at_head)


@app.route('/plot')
def plot():
    return render_template('plot.html', title='Plot')


@app.route('/plots/p2.png')
def p2_png():
    img = io.BytesIO()

    # matplot/ seaborn style setting
    sns.set_style('whitegrid')
    mpl.rcParams['patch.force_edgecolor'] = True
    sns.set(rc={'figure.figsize':(5.0, 5.0)})

    # QC group care about 'Run Finished Date'
    cols_keep = ['Lane Barcode',
                 'Midpool Library',
                 'Library',
                 'Run Finished Date',
                 'Total MB',
                 'Prefix',
                 'Group',
                 'Application',
                 'Numeric Total MB']

    df_ats = df_at[cols_keep]

    # groupby by Application
    df_appl = df_ats.groupby('Application')
    df_appl2 = (df_ats.groupby('Application')['Numeric Total MB'].sum()).reset_index()
    df_appl2['Total TB'] = (df_appl2['Numeric Total MB'] / 1000000)

    # Parameters for Application
    appl = df_appl2['Application']
    appl_sizes = df_appl2['Total TB']

    # chart by Application
    title = 'HGSC Illumina Distribution of Applications (2007-Present)'
    labels = appl
    sizes = appl_sizes

    # appl_pie
    p2 = make_pie(title, labels, sizes, 120, 9, 7)

    # TODO savefig
    p2.figure.tight_layout()
    p2.figure.savefig(img, format='png')

    # results
    png_data = img.getvalue()
    resp = make_response(png_data)
    resp.content_type = "image/png"
    return resp


    # groupby by Group
    df_grp = df_ats.groupby('Group')
    grp = df_grp['Group']
    df_grp2 = (df_ats.groupby('Group')['Numeric Total MB'].sum()).reset_index()
    df_grp2['Total TB'] = (df_grp2['Numeric Total MB'] / 1000000)

    # parameters for Group
    grp = df_grp2['Group']
    grp_sizes = df_grp2['Total TB']

    # chart by Group
    title = 'HGSC Illumina Distribution of Projects (2007-Present)'
    labels = grp
    sizes = grp_sizes

    # grp_pie
    p3 = make_pie(title,labels, sizes, 160, 20, 17)


# functions used for create pie chart
def make_pie(title, labels, sizes, angle, num_rows, explode_index):

    # explode index of the pie slice
    explode = make_explode(num_rows, explode_index)

    fig1, ax1 = plt.subplots()

    # turn off explode: explode=None
    ax1.pie(sizes,
            labels=labels,
            explode=explode,
            labeldistance=1.2,
            autopct='%1.1f%%',
            shadow=True,
            startangle=angle)

    # figure size
    params = {'figure.figsize': (12.6, 12.6)}
    pylab.rcParams.update(params)

    # set title
    fig1.suptitle(title, fontsize=20)

    # add legend
    plt.legend(labels, loc="upper right")

    # set color
    cs=cm.Set1(np.arange(40)/40.)

    # equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal');

    # TODO:
    # vertical callout label

    # TODO:
    # correct overlap labels

def make_explode(num_rows, explode_index):
    base = make_base(num_rows)
    base[explode_index] = 0.05
    return tuple(base)


def make_base(length):
    return [0,]*length


if __name__ == '__main__':
    initialize()
    app.run(debug=True)
