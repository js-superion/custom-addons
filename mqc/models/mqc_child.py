# -*- coding: utf-8 -*-
from openerp import models, fields

class Dialysis(models.Model):
    _name = "mqc.child" #child 儿科
    _description = u"儿科质控指标"
    _inherits = {'mqc.mqc': 'mqc_id'}
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                              ondelete='cascade')
    _rec_name = 'year_month'
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    mzrs = fields.Integer(u'门诊人数')
    zyrs = fields.Integer(u'住院人数')
    pjzyr = fields.Integer(u'平均住院日')
    avg_charge = fields.Float(u'术前平均住院日')
    avg_days = fields.Integer(u'门诊病人抗菌素使用率')
    accord_diag_case = fields.Integer(u'住院病人抗菌素使用率')
    kidney_exam_case = fields.Integer(u'医院感染发生率')
    exam_complications = fields.Integer(u'急危重抢救成功率')
    pressure_control_case = fields.Integer(u'住院病人人均费用')
    iga_rate = fields.Float(u'门诊病人人均费用')
    ln_rate = fields.Float(u'药占比(%)') #狼疮性肾炎lupus nephritis
    out_case1 = fields.Integer(u'抗菌药物DDD强度')

    cured_case = fields.Integer(u'住院患儿数')
    avg_charge1 = fields.Float(u'病理诊断率')
    avg_days1 = fields.Integer(u'治疗前诊断率')
    kidney_exam_case1 = fields.Integer(u'临床路径进入率')
    exam_complications1 = fields.Integer(u'微创手术率')
    finish_cp_case = fields.Integer(u'治疗有效率')#cp clinic pathway
    acpt_dialysis_case = fields.Float(u'手术并发症发生率(%)')
    out_case2 = fields.Integer(u'不良反应评估率')
    avg_charge2 = fields.Float(u'复发率')
    avg_days2 = fields.Integer(u'平均住院费用')

    cured_case = fields.Integer(u'住院患儿数')
    avg_charge1 = fields.Float(u'门诊空灌整复率')
    avg_days1 = fields.Integer(u'治疗前诊断率')
    kidney_exam_case1 = fields.Integer(u'临床路径进入率')
    exam_complications1 = fields.Integer(u'治疗有效率')
    finish_cp_case = fields.Integer(u'肠管坏死率')  # cp clinic pathway
    acpt_dialysis_case = fields.Float(u'手术并发症发生率(%)')
    out_case2 = fields.Integer(u'不良反应评估率')
    avg_charge2 = fields.Float(u'死亡率')
    avg_days2 = fields.Integer(u'平均住院费用')



    _sql_constraints = [
        ('year_month_uniq',
         'UNIQUE (year_month)',
         u'本月只能上报一次数据')
    ]

