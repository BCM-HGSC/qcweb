"""Code here is only about plotting. There should be no non-trivial
pandas code. There should be no Flask code."""

import io

from matplotlib import cm # color
import matplotlib as mpl
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


def plot_demo(data_frame):
    """Demonstrates a particular plot for a data frame. Returns tuple of
    image_data and image_type"""
    img = io.BytesIO()

    # matplot/ seaborn style setting
    sns.set_style('whitegrid')
    mpl.rcParams['patch.force_edgecolor'] = True
    sns.set(rc={'figure.figsize':(5.0, 5.0)})

    # seaborn countplot
    p1 = sns.countplot(x='Group', data=data_frame, palette='coolwarm')

    # rotate xticklabels to prevent the labels being overlapped
    p1.set_xticklabels(p1.get_xticklabels(), rotation=90);

    # adjust subplot params to avoid axis labels,titles or ticklabels being clipped
    p1.figure.tight_layout()
    p1.figure.savefig(img, format='png')

    # results
    plt.close()
    image_data = img.getvalue()
    img.close()
    image_type = "image/png"
    return image_data, image_type


def at_appl_plot(data_frame):
    img = io.BytesIO()

    # matplot/ seaborn style setting
    sns.set_style('whitegrid')
    mpl.rcParams['patch.force_edgecolor'] = True
    sns.set(rc={'figure.figsize':(10.6, 10.6)})

    # Parameters for Application
    appl = data_frame['Application']
    appl_sizes = data_frame['Total TB']

    # chart by Application
    title = 'HGSC Illumina Distribution of Applications (2007-Present)'
    labels = appl
    sizes = appl_sizes

    # appl_pie
    make_pie(title, labels, sizes, 120, 9, 7)

    # savefig
    # p1.figure.tight_layout()
    plt.savefig(img, format='png')

    # results
    plt.close()
    image_data = img.getvalue()
    img.close()
    image_type = "image/png"
    return image_data, image_type


def at_grp_plot(data_frame):

    # matplot/ seaborn style setting
    sns.set_style('whitegrid')
    mpl.rcParams['patch.force_edgecolor'] = True
    sns.set(rc={'figure.figsize':(10.6, 10.6)})

    # parameters for Group
    grp = data_frame['Group']
    grp_sizes = data_frame['Total TB']

    # chart by Group
    title = 'HGSC Illumina Distribution of Projects (2007-Present)'
    labels = grp
    sizes = grp_sizes

    # grp_pie
    p3 = make_pie(title,labels, sizes, 160, 20, 17)


# functions used to create pie chart
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

    # fig title parameters
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
