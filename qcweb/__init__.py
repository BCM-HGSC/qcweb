# First come standard libraries, in alphabetical order.
from datetime import date, time, datetime

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
from .data import my_data, CURRENT_COLUMNS_KEEP
from .selection import (limit_rows, head, sub_demo,
                        home_grp, home_appl,
                        query_ses, build_csv_data)
from .plotting import (plot_demo,
                       home_bar_plot, home_pie_plot,
                       bar_plot, grp_pie_plot, appl_pie_plot)
from .form_fields import QueryForm

# flask knows where to look for static & template files
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['WTF_CSRF_ENABLED'] = False


@app.route("/")
@app.route("/home")
def home():
    print('hello from /home')
    return render_template('home.html', title='Home')


@app.route("/home/plot1")
def home_p1_png():
    df_grp = home_grp()
    print(df_grp)
    image_data, image_type = home_bar_plot(df_grp)
    resp = make_response(image_data)
    resp.content_type = image_type
    return resp


@app.route("/home/plot2")
def home_p2_png():
    df_appl = home_appl()
    print(df_appl)
    image_data, image_type = home_pie_plot(df_appl)
    resp = make_response(image_data)
    resp.content_type = image_type
    return resp


@app.route("/table")
@app.route("/table/<start>")
@app.route("/table/<start>/<end>")
@app.route("/table/<start>/<end>/<platform>/<group>/<appl>/<qcreport>"
           "/<agg>/<display_table>")
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
    pl_url = url_for(
        'plot',
        platform=platform,
        group=group, appl=appl,
        start=start, end=end
    )
    return render_template('table.html', title='Table',
                           data=limit_rows(data)[CURRENT_COLUMNS_KEEP],
                           qcreport=qcreport, platform=platform,
                           group=group, appl=appl,
                           start=start, end=end,
                           agg=agg,
                           display_table=display_table,
                           num_rows=len(data),
                           dl_url=dl_url,
                           pl_url=pl_url)


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
        print(form.errors)
        if is_valid:
            print('It validated')
            flash(f'Query succussful {form.qcreport.data}!', category='success')
            # grab the data from the query on the form
            qcreport = form.qcreport.data
            platform = form.platform.data
            group = form.group.data
            appl = form.appl.data
            date_start = form.date_start.data
            time_start = parse_24h_time_str(form.time_start.data)
            start = datetime.combine(date_start, time_start)
            print('start: ', date_start, time_start, start, sep='\n')
            print(type(date_start), type(time_start), type(start))
            date_end = form.date_end.data
            time_end = parse_24h_time_str(form.time_end.data)
            end = datetime.combine(date_end, time_end)
            print('end: ', date_end, time_end, end, sep='\n')
            print(type(date_end), type(time_end), type(end))
            agg = form.agg.data
            plot_choice = form.plot_choice.data
            print('plot_choice: ',  plot_choice)
            print(type(plot_choice))
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
                return redirect(url_for("plot",
                                        qcreport=qcreport, platform=platform,
                                        group=group, appl=appl,
                                        start=start.isoformat(),
                                        end=end.isoformat(),
                                        agg=agg, plot_choice=plot_choice))
        assert not is_valid
        flash(f'Form not valid {form.qcreport.data}!', category='warning')
        print('back to query.html')
    return render_template('query.html', title='Query', form=form,
            error=form.errors)


def parse_24h_time_str(time_str):
    """Return `datetime.time`. Input in 24-hour HH:MM:SS format."""
    return time(*map(int, time_str.split(':')))


@app.route("/plot")
@app.route("/plot/<start>/<end>/<platform>/<group>/<appl>")
def plot(qcreport=None, platform=None,
         group=None, appl=None,
         start=None, end=None,
         agg=None, plot_choice=None):
    at = my_data.at
    data = query_ses(platform, group, appl, start, end)
    pl_url = url_for(
        'result_plot',
        data=data,
        platform=platform,
        group=group, appl=appl, start=start, end=end,
        plot_choice=plot_choice
    )
    return render_template('plot.html', title='Plot',
                           data=data, qcreport=qcreport,
                           platform=platform,
                           group=group, appl=appl,
                           start=start, end=end,
                           agg=agg, plot_choice=plot_choice,
                           plot_num_rows=len(data),
                           pl_url=pl_url)


@app.route("/result_plot")
@app.route("/result_plot/<start>/<end>/<platform>/<group>/<appl>")
def result_plot(
        platform=None,
        group=None, appl=None,
        start=None, end=None,
        # plot_choice=None
    ):
    at = my_data.at
    # plot_choice = plot_choice
    # print('result_plot_choice: ', plot_choice)
    data = query_ses(platform, group, appl, start, end)
    # call the logic here
    image_data, image_type = bar_plot(data)
    image_data, image_type = grp_pie_plot(data)
    image_data, image_type = appl_pie_plot(data)
    # image_data, image_type = get_plot_func(choice_dict[plot_choice])
    resp = make_response(image_data)
    resp.content_type = image_type
    return resp


choice_dict = {
        'Bar Plot': [bar_plot],
        'Group Pie Chart': [grp_pie_plot],
        'Application Pie Chart': [appl_pie_plot],
        'No Plot': [bar_plot]
}


def get_plot_func(func_list):
    for f in func_list:
        f(data)


@app.route("/plot/p1.png")
def p1_png():
    at_sub = sub_demo()
    image_data, image_type = plot_demo(at_sub)
    resp = make_response(image_data)
    resp.content_type = image_type
    return resp
