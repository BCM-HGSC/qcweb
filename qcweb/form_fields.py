import datetime
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField,
                     DateField, DateTimeField,
                     RadioField, SelectField, TextField,
                     TextAreaField, SubmitField, IntegerField)
from wtforms.validators import (DataRequired, InputRequired,
                                Optional, Length)
from wtforms_components import TimeField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


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
    time_start = TimeField(
        u'Time Start: ',
        validators=[Optional()],
        format='%H:%M:%S',
        default=datetime.datetime.strptime('00:00:00', '%H:%M:%S')
    )

    date_end = DateField(
        u'Date End: ',
        validators=[InputRequired("Please add an End Date.")],
        format='%Y-%m-%d'
    )
    time_end = TimeField(
        u'Time End: ',
        validators=[Optional()],
        format='%H:%M:%S',
        default=datetime.datetime.strptime('00:00:00', '%H:%M:%S')
    )
    # start = IntegerField()
    # end = IntegerField()

    # for pandas groupby filter
    agg = SelectField(
        u'Aggregation: ',
        validators=[InputRequired("Please choose an Aggregation.")],
        choices=[('do_not_agg', 'Do Not Aggregate'),
                 ('by_group', 'By Group'),
                 ('by_appl', 'By Application')],
        default='do_not_agg'
    )

    # graphs QC group presents and routinely uses
    # plot_choice = SelectField(
    #    u'Plot Choice:',
    #    choices=[('plot_one', '10X-20X-30X cov chart'),
    #             ('plot_two', 'Coverage Distribution'),
    #             ('plot_three', 'Recent 75-ples')]
    # )

    # display_table  = BooleanField("Display Table: ")
    display_table = RadioField(
        'Display Table:',
        validators=[InputRequired("Please choose Yes or No.")],
        choices=[('Yes', 'Yes'), ('No', 'No')],
        default='Yes'
    )

    submit = SubmitField('Submit')
