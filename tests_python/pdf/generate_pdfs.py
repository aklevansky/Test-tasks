# -*- coding: utf-8 -*-
import os
import csv

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape, portrait
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from mxdata import (where,
                    when,
                    program,
                    module,
                    volume,
                    director,
                    some_boss,
                    city,
                    diploma_info,
                    reg_number,
                    stylesheet)


pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'Arial Bold.ttf'))


def build_diploma(person_data):
    diploma_fname = 'diplom%s.pdf' % person_data['diploma_id']
    path_to_diploma = os.path.join('diplomas', diploma_fname)

    c = canvas.Canvas(path_to_diploma, pagesize=landscape(A4), bottomup=0)

    person_text = '%(family)s %(name)s %(patronymic)s' % person_data
    person_para = Paragraph(person_text, stylesheet()['person_name'])
    person_para.wrapOn(c, 200, 100)
    person_para.drawOn(c, 600, 300)

    where_text = 'прошел(а) обучение в %(where)s' % where
    where_para = Paragraph(where_text, stylesheet()['default'])
    where_para.wrapOn(c, 300, 600)
    where_para.drawOn(c, 300, 600)

    when_text = 'c «%(when_begin_day)s» %(when_begin_month)s %(when_begin_year)s \
    по «%(when_end_day)s» %(when_end_month)s %(when_end_year)s' % when
    when_para = Paragraph(when_text, stylesheet()['default'])
    when_para.wrapOn(c, 300, 600)
    when_para.drawOn(c, 300, 600)

    program_para = Paragraph(program, stylesheet()['default'])
    program_para.wrapOn(c, 300, 600)
    program_para.drawOn(c, 10, 20)

    module_para = Paragraph(module, stylesheet()['default'])
    module_para.wrapOn(c, 300, 600)
    module_para.drawOn(c, 10, 20)

    volume_para = Paragraph(volume, stylesheet()['default'])
    volume_para.wrapOn(c, 300, 600)
    volume_para.drawOn(c, 10, 20)

    director_para = Paragraph(director, stylesheet()['default'])
    director_para.wrapOn(c, 300, 600)
    director_para.drawOn(c, 10, 20)

    some_boss_para = Paragraph(some_boss, stylesheet()['default'])
    some_boss_para.wrapOn(c, 300, 600)
    some_boss_para.drawOn(c, 10, 20)

    city_para = Paragraph(city, stylesheet()['default'])
    city_para.wrapOn(c, 300, 600)
    city_para.drawOn(c, 10, 20)

    diploma_info_para = Paragraph(diploma_info, stylesheet()['default'])
    diploma_info_para.wrapOn(c, 300, 600)
    diploma_info_para.drawOn(c, 10, 20)

    reg_number_para = Paragraph(reg_number, stylesheet()['default'])
    reg_number_para.wrapOn(c, 300, 600)
    reg_number_para.drawOn(c, 10, 20)

    c.save()


if __name__ == '__main__':
    # fname = raw_input('Введите путь к файлу с исходными данными: ')
    fname = 'persons.csv'
    if not os.path.exists(fname):
        print('Файл %s не найден' % fname)
        exit()
    with open(fname) as f:
        reader = csv.DictReader(f, delimiter=',')
        for person_data in reader:
            build_diploma(person_data)
