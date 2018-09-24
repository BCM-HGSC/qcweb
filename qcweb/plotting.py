"""Code here is only about plotting. There should be no non-trivial
pandas code. There should be no Flask code."""

import io

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


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


def grp_bar_plot(data_frame):
    img = io.BytesIO()

    # seaborn style setting
    sns.set_style('whitegrid')
    sns.set(rc={'figure.figsize':(7.0, 4.5)})

    # parameters for grp
    grp = data_frame['grp']
    grp_sizes = data_frame['grp_sizes']

    # seaborn barplot
    p1 = sns.barplot(x='grp',y='grp_sizes',data=data_frame, palette='coolwarm')
    p1.set_xlabel('Group')
    p1.set_ylabel('Total TB');
    p1.set_xticklabels(p1.get_xticklabels(),rotation=90)

    # save plot
    p1.figure.tight_layout()
    p1.figure.savefig(img, format='png')

    # results
    plt.close()
    image_data = img.getvalue()
    img.close()
    image_type = "image/png"
    return image_data, image_type

def appl_pie_plot(data_frame):
    img = io.BytesIO()

    # matplot/ seaborn style setting
    sns.set_style('whitegrid')
    mpl.rcParams['patch.force_edgecolor'] = True
    sns.set(rc={'figure.figsize':(2.5, 2.5)})

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
