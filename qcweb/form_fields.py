import datetime
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateField, HiddenField,
                     RadioField, SelectField, TextField,
                     TextAreaField, SubmitField, IntegerField)
from wtforms.validators import (DataRequired, InputRequired,
                                Length, Regexp)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

TIME_24HOUR_REGEX = '([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]'


# create a WTForm Class
class QueryForm(FlaskForm):
    '''
    This class will be updated when we have more input from QC group.
    '''
    qcreport = StringField(
        'Type of QC Report: ',
        validators=[DataRequired(), Length(min=2, max=20)]
    )

    platform = SelectField(
        u'Platform: ',
        validators=[InputRequired("Please choose a Platform.")],
        choices=[('Any', 'Any'),
                 ('NovaSeq', 'NovaSeq'),
                 ('HiSeq X', 'HiSeq X'),
                 ('MiSeq', 'MiSeq'),
                 ('HiSeq 2000', 'HiSeq 2000'),
                 ('HiSeq 2500', 'HiSeq 2500'),
                 ('GA', 'GA')],
        default='Any'
    )

    group = SelectField(
        u'Group: ',
        validators=[InputRequired("Please choose a Group.")],
        choices=[('Any', 'Any'),
                 ('ADSP', 'ADSP'),
                 ('BAC', 'BAC'),
                 ('CCDG', 'CCDG'),
                 ('CHARGE', 'CHARGE'),
                 ('Cancer', 'Cancer'),
                 ('Comparative', 'Comparative'),
                 ('Complex Disease', 'Complex Disease'),
                 ('Gabriella', 'Gabriella'),
                 ('H3 Africa', 'H3 Africa'),
                 ('Insects', 'Insects'),
                 ('Mendelian', 'Mendelian'),
                 ('Metagenomic', 'Metagenomic'),
                 ('Other', 'Other'),
                 ('Research & Development', 'Research & Development'),
                 ('Rui Chen', 'Rui Chen'),
                 ('TCGA', 'TCGA'),
                 ('TEDDY', 'TEDDY'),
                 ('TG', 'TG'),
                 ('TOPMed', 'TOPMed'),
                 ('Virology & Microbiology', 'Virology & Microbiology')],
        default='Any'
    )

    appl = SelectField(
        u'Application: ',
        validators=[InputRequired("Please choose a Application.")],
        choices=[('Any', 'Any'),
                 ('Amplicon Pool', 'Amplicon Pool'),
                 ('CHIP-Seq', 'CHIP-Seq'),
                 ('R & D', 'R & D'),
                 ('RNA Req', 'RNA Seq'),
                 ('RNA Seq Capture', 'RNA Seq Capture'),
                 ('Regional capture', 'Reginal capture'),
                 ('Whole EXOME', 'Whole EXOME'),
                 ('Whole Genome', 'Whole Gemone'),
                 ('small RNA', 'small RNA')],
        default='Any'
    )

    # QC group care about Run Finished Date
    date_start = DateField(
        u'Date Start: ',
        validators=[InputRequired("Please add a Start Date.")],
        format='%Y-%m-%d'
    )
    time_start = StringField(
        u'Time Start: ',
        validators=[Regexp(TIME_24HOUR_REGEX, message='24-hour HH:MM:SS')],
        default='00:00:00'
    )

    date_end = DateField(
        u'Date End: ',
        validators=[InputRequired("Please add an End Date.")],
        format='%Y-%m-%d'
    )
    time_end = StringField(
        u'Time End: ',
        validators=[Regexp(TIME_24HOUR_REGEX, message='24-hour HH:MM:SS')],
        default='00:00:00'
    )
    # start = IntegerField()
    # end = IntegerField()

    # for pandas groupby filter
    agg = SelectField(
        u'Aggregation: ',
        validators=[InputRequired("Please choose an Aggregation.")],
        choices=[('Do Not Aggregate', 'Do Not Aggregate'),
                 ('By Group', 'By Group'),
                 ('By Application', 'By Application')],
        default='Do Not Aggregate'
    )

    submit = SubmitField('Submit')


class PlotForm(FlaskForm):
    # graphs QC group presents and routinely uses
    start = HiddenField('start')
    end = HiddenField('end')
    platform = HiddenField('platform')
    group = HiddenField('group')
    appl = HiddenField('appl')
    plot_choice = SelectField(
       u'Plot Choice:',
       choices=[('Bar Plot', 'Bar Plot'),
                ('Group Pie Chart', 'Group Pie Chart'),
                ('Application Pie Chart', 'Application Pie Chart')],
       default='Bar Plot'
    )

    submit = SubmitField('Plot')
