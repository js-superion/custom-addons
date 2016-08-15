# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Blood(models.Model):
    _name = "mqc.blood.clinic"
    _description = u'全院临床用血情况'

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

class BloodTech(models.Model):
    _name = "mqc.blood"
    _description = u"输血填报"
    _inherits = {'mqc.mqc': 'mqc_id'}
    # _inherit = 'mqc.mqc'
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                              ondelete='cascade')
    report_construct = fields.Many2one('mqc.blood.construct', u'输血科建设及检测技术')
    report_clinic = fields.Many2one('mqc.blood.clinic', u'全院临床用血情况')



class BloodTech(models.Model):
    _name = "mqc.blood.tech"
    _description = u"输血科检测技术"
    name = fields.Char(u'技术名称',)
    tech_method = fields.Char(u'操作方法',)


class BloodConstructDetail(models.Model):
    _name = "mqc.blood.construct.detail"
    _description = u"输血科建设及检测技术明细"
    tech_id = fields.Many2one('mqc.blood.tech',u'输血科检测技术',required=True, )
    construct_id = fields.Many2one('mqc.blood.construct',u'主记录',required=True, )
    #关联技术字典
    tech_name = fields.Char(
        u'技术名称',
        related='tech_id.name',
        readonly=False, store=True,
    )
    opr_method = fields.Char(
        u'操作方法',
        related='tech_id.tech_method',
        readonly=False, store=True,
    )

    cases = fields.Integer(u'例数', )
    indoor_qc_freq = fields.Integer(u'室内质控频率', )
    province_eqa = fields.Char(u'省室间质评结果', ) #eqa = external quality assessment
    country_eqa = fields.Char(u'国室间质评结果', )

class BloodConstruct(models.Model):
    _name = "mqc.blood.construct"
    _description = u'输血科建设及检测技术'
    # _inherits = {'mqc.mqc': 'mqc_id'}
    # mqc_id = fields.Many2one('mqc.mqc', '报表id', required=True,
    #                           ondelete='cascade')
    report_month = fields.Char( u'上报月份',)
    units_name = fields.Char( u'单位名称',)
    units_code = fields.Char(u'单位编码',)
    create_type = fields.Selection([('01', u'独立建制'),('02', u'未设独立建制'),],
                                   u'输血科或血库建制')
    dept_emp_num = fields.Integer(u'科室人数',)
    bed_num = fields.Integer( u'医院床位数',)
    required_device  = fields.Selection([('01', u'齐全'),('02', u'不齐全'),],u'科室必需设备',)
    shortage_device = fields.Char(u'缺少的设备名称',)
    detail_ids = fields.One2many('mqc.blood.construct.detail', 'construct_id', u'技术明细')


