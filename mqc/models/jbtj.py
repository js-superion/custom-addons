# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Jbtj(models.Model):
    _name = "test.jbtj"
    _description = u'加班统计'

    report_month = fields.Date(
        u'加班日期',
    )
    content = fields.Text(
        u'工作内容',
    )
    start_date = fields.Datetime(
        u'开始时间',
    )

    end_date = fields.Datetime(
        u'结束时间',
    )
    total_time = fields.Integer(
        u'总时长',
    )

