"""Code here is only about plotting. There should be no non-trivial
pandas code. There should be no Flask code."""

import io

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns; sns.set_style('whitegrid')

from matplotlib import cm # color

from .data import my_data

def plot_demo(data_frame):
    """Demonstrates a particular plot for a data frame. Returns tuple of
    image_data and image_type"""
    img = io.BytesIO()

    # matplot/ seaborn style setting
    mpl.rcParams['patch.force_edgecolor'] = True
    sns.set(rc={'figure.figsize': (5.0, 5.0)})

    # seaborn countplot
    p1 = sns.countplot(x='Group', data=data_frame, palette='coolwarm')

    # rotate xticklabels to prevent the labels being overlapped
    p1.set_xticklabels(p1.get_xticklabels(), rotation=90)

    # adjust subplot params
    # to avoid axis labels,titles or ticklabels being clipped
    p1.figure.tight_layout()
    p1.figure.savefig(img, format='png')

    # results
    plt.close()
    image_data = img.getvalue()
    img.close()
    image_type = "image/png"
    return image_data, image_type


def home_bar_plot(data_frame):
    img = io.BytesIO()

    # seaborn style setting
    sns.set_style('whitegrid')
    sns.set(rc={'figure.figsize': (7.0, 4.5)})

    # parameters for grp
    grp = data_frame['grp']
    grp_sizes = data_frame['grp_sizes']

    # seaborn barplot
    p1 = sns.barplot(x='grp', y='grp_sizes',
                     data=data_frame, palette='coolwarm')
    p1.set_xlabel('Group')
    p1.set_ylabel('Total TB')
    p1.set_xticklabels(p1.get_xticklabels(), rotation=90)

    # save plot
    p1.figure.tight_layout()
    p1.figure.savefig(img, format='png')

    # results
    plt.close()
    image_data = img.getvalue()
    img.close()
    image_type = "image/png"
    return image_data, image_type


def home_pie_plot(data_frame):
    img = io.BytesIO()

    # matplot/ seaborn style setting
    sns.set_style('whitegrid')
    mpl.rcParams['patch.force_edgecolor'] = True
    sns.set(rc={'figure.figsize': (2.5, 2.5)})

    # returns a list of values
    appl = data_frame['appl'].tolist()
    appl_sizes = data_frame['appl_sizes'].tolist()

    # pie chart, where the slices will be ordered and plotted counter-clockwise
    labels = appl
    sizes = appl_sizes

    # only "explode" one slice (eg 'Whole EXOME')
    explode = (0, 0.1, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            labeldistance=1.2, wedgeprops={'linewidth': 0.8, 'edgecolor': 'w'},
            shadow=True, startangle=90)
    ax1.axis('equal')

    # savefig
    fig1.tight_layout()
    plt.savefig(img, format='png', bbox_inches='tight')

    # results
    plt.close()
    image_data = img.getvalue()
    img.close()
    image_type = "image/png"
    return image_data, image_type


def bar_plot(data_frame):
    """input is query data_frame and output is seaborn countplot"""
    img = io.BytesIO()

    # matplot/ seaborn setting
    mpl.rcParams['patch.force_edgecolor'] = True
    sns.set(rc={'figure.figsize': (10, 6)}) # figure size in inches

    # order = data_frane['Group'].value_counts().index # query data
    at = my_data.at # all time data
    order = at['Group'].value_counts().index

    # seaborn countplot
    p1 = sns.countplot(x='Group',
                      data=data_frame,
                      # hue='Group',
                      palette='coolwarm',
                      order = order)

    # rotation xlabels to prevent the labels being overlapped
    p1.set_xticklabels(p1.get_xticklabels(), rotation=-45)

    # adjust subplot params
    # to avoid axis labels, titles or ticklabels being clipped
    p1.figure.tight_layout()
    p1.figure.savefig(img, format='png')

    # put legend out of the figure when hue is turned on
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)

    # results
    plt.close()
    image_data = img.getvalue()
    img.close()
    image_type = "image/png"
    return image_data, image_type


def grp_pie_plot(data_frame):
    img = io.BytesIO()

    # the slices will be ordered and plotted counter-clockwise
    grp = data_frame.groupby('Group')
    grp2 = (data_frame.groupby('Group')['TOTAL_MB'].sum()).reset_index()
    grp2['Total TB'] = (grp2['TOTAL_MB'] / 1_000_000)
    grp3 = grp2
    # grp3 = grp2[grp2['Total TB'] > 100] # filter out negligence

    grp = grp3['Group']
    grp_sizes = grp3['Total TB']

    # parameters for make_pie
    title = "Pie Chart by Group"
    labels = grp
    sizes = grp_sizes
    num_rows = len(grp3)
    explode_index = 0
    angle = 100

    make_pie(title, labels, sizes, num_rows, explode_index, angle)

    # resize the figure box
    # similar to calling figure.tight_layout()
    plt.savefig(img, format='png', bbox_inches='tight')

    # results
    plt.close()
    image_data = img.getvalue()
    img.close()
    image_type = "image/png"
    return image_data, image_type


def appl_pie_plot(data_frame):
    img = io.BytesIO()

    # the slices will be ordered and plotted counter-clockwise:
    appl = data_frame.groupby('Application')
    appl2 = (data_frame.groupby('Application')['TOTAL_MB'].sum()).reset_index()
    appl2['Total TB'] = (appl2['TOTAL_MB'] / 1_000_000)
    appl3 = appl2
    # appl3 = appl2[appl2['Total TB'] > 10] # filter out negligence

    appl = appl3['Application']
    appl_sizes = appl3['Total TB']

    # parameters for make_pie
    title = "Pie Chart by Application"
    labels = appl
    sizes = appl_sizes
    num_rows = len(appl3)
    explode_index = 0
    angle = 110

    make_pie(title, labels, sizes, num_rows, explode_index, angle)

    # resize the figure box
    # similar to calling figure.tight_layout()
    plt.savefig(img, format='png', bbox_inches='tight')

    # results
    plt.close()
    image_data = img.getvalue()
    img.close()
    image_type = "image/png"
    return image_data, image_type


def make_pie(title, labels, sizes, num_rows, explode_index, angle):
    # explode index of the pie slice
    explode = make_explode(num_rows, explode_index)

    fig1, ax1 = plt.subplots()

    # set explode=None to turn off
    ax1.pie(sizes, labels=labels, labeldistance=1.2,
            explode=explode, autopct='%1.1f%%',
            shadow=True, startangle=angle)

    # matplot/ seaborn style setting
    mpl.rcParams['patch.force_edgecolor'] = True
    plt.rcParams["figure.figsize"] = (4, 4) # set fig size in inches

    # fig title
    fig1.suptitle(title, fontsize=13)

    # legend options
    # bbox_to_anchor(x0, y0, width, height)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    # set color
    cs=cm.Set1(np.arange(40)/40.)

    # equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')

    # TODO vertical call out labels

    # TODO correct overlap labels


def make_explode(num_rows, explode_index):
    base = make_base(num_rows)
    base[explode_index] = 0.05
    return tuple(base)


def make_base(length):
    return [0,]*length
