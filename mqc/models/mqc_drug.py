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
    antibiotics_use_rate = fields.Float(u'中药饮片配方总量误差') #
    cp_disease = fields.Float(u'调配药品用法用量标识率') #
    dispute_case = fields.Integer(u'一级药库盘点误差率')
    attacked_case = fields.Float(u'二级药库盘点误差率')
    attacked_case = fields.Float(u'“五专”管理合格率')
    attacked_case = fields.Float(u'"四专"管理合格率')
    attacked_case = fields.Float(u'麻精药品帐物相符率')
    attacked_case = fields.Float(u'麻精药品处方调配合格率')
    attacked_case = fields.Float(u'门、急诊处方点评抽样率')
    attacked_case = fields.Float(u'点评出院病历数')
    attacked_case = fields.Float(u'点评的处方合格率')
    attacked_case = fields.Float(u'填报不良反应数')
    attacked_case = fields.Float(u'严重药品不良反应报告数量')
    attacked_case = fields.Float(u'药占比')
    attacked_case = fields.Float(u'每次就诊人均药费')
    attacked_case = fields.Float(u'就诊使用抗菌药物的百分率')
    attacked_case = fields.Float(u'就诊使用注射药物的百分率')
    attacked_case = fields.Float(u'就诊使用中药注射剂的百分率')
    attacked_case = fields.Float(u'就诊使用国家基本药物的百分率')
    attacked_case = fields.Float(u'独立的临床药学工作室数量')
    attacked_case = fields.Float(u'药学专业技术人员比例')

    # 专业信息（抗菌药物）
    attacked_case = fields.Float(u'执行抗菌药物分级管理合格率')
    attacked_case = fields.Float(u'抗菌药物品种品规合格率')
    attacked_case = fields.Float(u'抗菌药物处方合格率')
    attacked_case = fields.Float(u'住院患者抗菌药物使用率')
    attacked_case = fields.Float(u'住院患者抗菌药物使用强度')
    attacked_case = fields.Float(u'住院患者人均使用抗菌药物费用')
    attacked_case = fields.Float(u'抗菌药物费用占总药费的百分率')
    attacked_case = fields.Float(u'抗菌药物处方比例')
    attacked_case = fields.Float(u'开展抗菌药物处方点评工作')
    attacked_case = fields.Float(u'开展清洁手术预防用抗菌药物点评工作')

    attacked_case = fields.Float(u'"特殊使用"抗菌药物用量占抗菌药物用量的百分率')
    attacked_case = fields.Float(u'介入手术诊断抗菌药物预防使用率')
    attacked_case = fields.Float(u'清洁手术抗菌药物预防使用率')
    attacked_case = fields.Float(u'清洁手术预防给药合格率（0.5 - 2h）')
    attacked_case = fields.Float(u'清洁手术预防给药品种合格率')
    attacked_case = fields.Float(u'清洁手术预防给药疗程合格率')
    attacked_case = fields.Float(u'清洁手术预防给药联合用药率')
    attacked_case = fields.Float(u'住院患者抗菌药物病原学送检率')
    attacked_case = fields.Float(u'限制性使用抗菌药物病原学送检率')
    attacked_case = fields.Float(u'特殊使用抗菌药物病原学送检率')
    # 专业信息（临床药学）
    attacked_case = fields.Float(u'专职临床药师数量')
    attacked_case = fields.Float(u'参与的科室数量')
    attacked_case = fields.Float(u'参与管理的病种数量')
    attacked_case = fields.Float(u'开展病例讨论数量')
    attacked_case = fields.Float(u'开展用药教育数量')
    attacked_case = fields.Float(u'开展药物咨询数量')
    attacked_case = fields.Float(u'开展处方点评数量')
    attacked_case = fields.Float(u'开展医嘱点评数量')
    attacked_case = fields.Float(u'参与临床会诊数量')
    attacked_case = fields.Float(u'开展处方点评数量')

    attacked_case = fields.Float(u'书写药历数量')
    attacked_case = fields.Float(u'书写疑难病历以及分析数量')
    attacked_case = fields.Float(u'书写用药教育数量')
    attacked_case = fields.Float(u'进行用药指导数量')
    attacked_case = fields.Float(u'进行治疗药物监测')
    attacked_case = fields.Float(u'TDM品种数量')
    attacked_case = fields.Float(u'临床药师工作时间')
    attacked_case = fields.Float(u'开展日常查房工作')
    attacked_case = fields.Float(u'开展抗菌药物临床使用管理')

    _sql_constraints = [
        ('year_month_uniq',
         'UNIQUE (year_month)',
         u'本月只能上报一次数据')
    ]
