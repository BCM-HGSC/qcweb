# First come standard libraries, in alphabetical order.

# After a blank line, import third-party libraries.
from flask import Flask
from flask import flash
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_wtf import FlaskForm
from wtforms import (BooleanField, DateField, DateTimeField,
                     RadioField, SelectField, StringField,
                     SubmitField, TextAreaField, TextField,
                     ValidationError)

from wtforms.validators import DataRequired

# After another blank line, import local libraries.
from .data import CURRENT_COLUMNS_KEEP
from .selection import (limit_rows, head, sub_demo,
                        home_grp, home_appl,
                        query_ses, build_csv_data)
from .plotting import plot_demo, grp_bar_plot, appl_pie_plot
from .form_fields import QueryForm

# flask knows where to look for static & template files
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route("/")
@app.route("/home")
def home():
    print('hello from /home')
    return render_template('home.html', title='Home')


@app.route("/home/plot1")
def home_p1_png():
    df_grp = home_grp()
    print(df_grp)
    image_data, image_type = grp_bar_plot(df_grp)
    resp = make_response(image_data)
    resp.content_type = image_type
    return resp


@app.route("/home/plot2")
def home_p2_png():
    df_appl = home_appl()
    print(df_appl)
    image_data, image_type = appl_pie_plot(df_appl)
    resp = make_response(image_data)
    resp.content_type = image_type
    return resp


@app.route("/table")
@app.route("/table/<start>")
@app.route("/table/<start>/<end>")
@app.route("/table/<start>/<end>/<platform>/<group>/<appl>")
def table(qcreport=None, platform=None,
          group=None, appl=None,
          start=None, end=None,
          agg=None, display_table=None):
    data = query_ses(platform, group, appl, start, end)
    dl_url = url_for(
        'table_download',
        platform=platform,
        group=group, appl=appl,
        start=start, end=end
    )
    return render_template('table.html', title='Table',
                           data=limit_rows(data)[CURRENT_COLUMNS_KEEP],
                           qcreport=qcreport, platform=platform,
                           group=group, appl=appl,
                           start=start, end=end,
                           agg=agg, display_table=display_table,
                           num_rows=len(data),
                           dl_url=dl_url)


CSV_TYPE = 'text/csv'


@app.route("/table-download")
@app.route("/table-download/<start>/<end>/<platform>/<group>/<appl>")
def table_download(
        platform=None,
        group=None, appl=None,
        start=None, end=None,
        # agg=None
    ):
    data = query_ses(platform, group, appl, start, end)
    csv_data = build_csv_data(data)
    resp = make_response(csv_data)
    resp.content_type = CSV_TYPE
    return resp


@app.route("/query", methods=['GET', 'POST'])
def query():
    print('hello from /query')
    # create instance of the form
    form = QueryForm(request.form)
    if request.method == 'POST':
        # if the form is valid on submission
        is_valid = form.validate_on_submit()
        print('validation result', is_valid)
        if is_valid:
            print('It validated')
            flash(f'Query succussful {form.qcreport.data}!', 'success')
            # grab the data from the query on the form
            qcreport = form.qcreport.data
            platform = form.platform.data
            group = form.group.data
            appl = form.appl.data
            start = form.start.data
            end = form.end.data
            agg = form.agg.data
            # plot_choice = form.plot_choice.data
            display_table = form.display_table.data
            want_table = True  # TODO: make False based on form
            print('results')
            if want_table:
                print(start)
                print(type(start))
                return redirect(url_for("table",
                                        qcreport=qcreport, platform=platform,
                                        group=group, appl=appl,
                                        start=start.isoformat(),
                                        end=end.isoformat(),
                                        agg=agg, display_table=display_table))
            else:
                return redirect(url_for("plot"))
        assert not is_valid
        flash(f'Form not valid {form.qcreport.data}!', 'warning')
        print('back to query.html')
    return render_template('query.html', title='Query', form=form,
            error=form.errors)


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
