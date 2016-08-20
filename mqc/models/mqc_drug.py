# -*- coding: utf-8 -*-
from openerp import models, fields

class Drug(models.Model):
    _name = "mqc.drug" # 药事管理指标
    _description = u"药事管理指标"
    _inherits = {'mqc.mqc': 'mqc_id'}
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                              ondelete='cascade')
    year_month = fields.Char(u'年月', default=lambda self: self.env['utils'].get_zero_time().strftime('%Y-%m'))
    _rec_name = 'year_month'

    #1、一 般信息：
    outpat_capacity = fields.Integer(u'临床药品紧缺数量')
    discharged_case = fields.Integer(u'药品采供率')
    accord_diag_case = fields.Float(u'一品两规符合率')
    rescue_rate = fields.Float(u'阳光采购得分')
    avg_adm_days = fields.Integer(u'医师签名与药房留样符合率')
    bed_use_rate = fields.Float(u'药品使用通用名率')
    mr_grade_a_rate = fields.Float(u'门诊处方复核率')
    opr_three_four = fields.Integer(u'普通处方调配合格率')
    unplanned_opr_two = fields.Float(u'调配药品的出门差错率/例')
    antibiotics_use_rate = fields.Float(u'中药饮片配方总量误差') #antibiotics抗生素
    cp_disease = fields.Float(u'调配药品用法用量标识率') #cp clinic path
    dispute_case = fields.Integer(u'一级药库盘点误差率')
    attacked_case = fields.Float(u'二级药库盘点误差率')
    attacked_case = fields.Float(u'“五专”管理合格率')
    attacked_case = fields.Float(u'二级药库盘点误差率')
    attacked_case = fields.Float(u'二级药库盘点误差率')

    #4、落实患者安全目标（是/否）：
    protect_pat1 = fields.Selection([('1', u'是'), ('0', u'否')],u'是否落实手术安全核查、风险评估、术者亲自沟通制度')
    protect_pat2 = fields.Selection([('1', u'是'), ('0', u'否')],u'是否有患者身份识别与手术部位标识')
    protect_pat3 = fields.Selection([('1', u'是'), ('0', u'否')],u'是否主动报告医疗隐患、医疗不良事件')

    _sql_constraints = [
        ('year_month_uniq',
         'UNIQUE (year_month)',
         u'本月只能上报一次数据')
    ]
