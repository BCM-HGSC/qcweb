from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField,
                     DateField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired


app.config['SECRET_KEY'] = 'mysecretkey'


# create a WTForm Class
class QueryForm(FlaskForm):
    '''
    This class will be updated when we have more input from QC group.
    '''
    qcreport = StringField('QC Report',validators=[DataRequired()])
    platform = SelectField(u'Platform: ',
                    choices=[('NovaSeq', 'NovaSeq'),
                             ('HiSeq X' 'HiSeq X'),
                             ('MiSeq', 'MiSeq'),
                             ('HiSeq 2000', 'HiSeq 2000'),
                             ('HiSeq 2500', 'HiSeq 2500')])

    group = SelectField(u'Group: ',
                    choices=[('ADSP', 'ADSP'),
                             ('BAC', 'BAC'),
                             ('CCDG', 'CCDG'),
                             ('CHARGE', 'CHARGE'),
                             ('Cancer', 'Cancer'),
                             ('Comparative', 'Comparative'),
                             ('Complex Disease', 'Complex Disease'),
                             ('Gabriella', 'Gabriella'),
                             ('H3 Africa', 'H3 Africa'),
                             ('Insects', 'Insects'),
                             ('Mendelian', 'Medelian'),
                             ('Metagenomic', 'Metagenomic'),
                             ('Other', 'Other'),
                             ('Research & Development', 'Research & Development'),
                             ('Rui Chen', 'Rui Chen'),
                             ('TCGA', 'TCGA'),
                             ('TEDDY', 'TEDDY'),
                             ('TG', 'TG'),
                             ('TOPMed', 'TOPMed'),
                             ('Virology & Microbiology', 'Virology & Microbiology')])

    appl = SelectField(u'Application: ',
                    choices=[('Amplicon Pool', 'Amplicon Pool'),
                             ('CHIP-Seq', 'CHIP-Seq'),
                             ('R & D', 'R & D'),
                             ('RNA Req', 'RNA Seq'),
                             ('RNA Seq Capture', 'RNA Seq Capture'),
                             ('Regional capture', 'Reginal capture'),
                             ('Whole EXOME', 'Whole EXOME'),
                             ('Whole Genome', 'Whole Gemone'),
                             ('small RNA', 'small RNA')])

    # QC group care about 'Run Finished Date'
    start = DateField(format='%Y-%m-%d')
    end = DateField(format='%Y-%m-%d')

    # for pandas groupby filter
    agg = SelectField(u'Aggregation: ',
                choices=[('by_group', 'By Group'),
                         ('by_appl', 'By Application')])

    # graphs QC group presents and routinely uses
    plot_choice = SelectField(u'Plot Choice:',
                          choices=[('plot_one', '10X-20X-30X cov chart'),
                                   ('plot_two', 'Coverage Distribution'),
                                   ('plot_three', 'Recent 75-ples')])

    # display_table  = BooleanField("Display Table: ")
    display_table = RadioField('Display Table:', choices=[('yes','Yes'), ('no','No')])

    submit = SubmitField('Submit')
