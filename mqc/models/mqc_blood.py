# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Blood(models.Model):
    _name = "mqc.blood"
    _description = u'用血质控指标'

    report_month = fields.Char(
        u'上报月份',
    )
    units_name = fields.Char(
        u'单位名称',
    )
    units_code = fields.Char(
        u'单位编码',
    )

    out_case = fields.Integer(
        u'出院总人数',
    )
    use_blood_case = fields.Integer(
        u'用血总人数',
    )
    opr_num  = fields.Integer(
        u'手术台数',
    )
    opr_use_blood = fields.Integer(
        u'手术用血人数',
    )
    whole_blood = fields.Integer(
        u'全血',
    )
    short_sign1 = fields.Char(
        u'全血是否短缺',
    )
    rbc = fields.Integer(
        u'红细胞',
    )
    short_sign2 = fields.Char(
        u'红细胞是否短缺',
    )
    plasma = fields.Integer(
        u'血浆',
    )
    short_sign3 = fields.Char(
        u'血浆是否短缺',
    )
    platelet = fields.Integer(
        u'血小板',
    )
    short_sign4 = fields.Char(
        u'血小板是否短缺',
    )
    cryoprecipitate = fields.Integer(
        u'冷沉淀',
    )
    short_sign5 = fields.Char(
        u'冷沉淀是否短缺',
    )

    total_usage = fields.Integer(
        u'本月用血量合计',
    )
    self_storage = fields.Integer(
        u'储存式',
    )
    self_storage_case = fields.Integer(
        u'储存式人数',
    )
    self_recycle = fields.Float(
        u'回收式',
    )
    self_recycle_case = fields.Integer(
        u'回收式人数',
    )
    dilution = fields.Integer(
        u'稀释式',
    )
    dilution_case = fields.Integer(
        u'稀释式人数',
    )
    total_self_usage = fields.Integer(
        u'自体输血量',
    )
    total_self_case = fields.Integer(
        u'自体输血数',
    )
    component_rate = fields.Integer(
        u'成分输血率',
    )
    self_rate = fields.Integer(
        u'自体输血率',
    )
    avg_usage= fields.Integer(
        u'住（出）院患者人均用血量',
    )

