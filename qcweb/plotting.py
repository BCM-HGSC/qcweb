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
