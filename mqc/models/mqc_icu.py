# -*- coding: utf-8 -*-
from openerp import models, fields

class Icu(models.Model):
    _name = "mqc.icu"
    _description = u"ICU填报"
    _inherits = {'mqc.mqc': 'mqc_id'}
    mqc_id = fields.Many2one('mqc.mqc', u'报表id', required=True,
                              ondelete='cascade')
    treated_rate = fields.Integer(u'ICU 患者收治率', )
    apache2_excess15 = fields.Integer(u'急性生理与慢性健康评分（APACHE II 评分）≥15分患者收治率', )
    joint_rounds = fields.Integer(u'多学科联合查房率', )
    exam_rate = fields.Integer(u'抗菌药物治疗前病原学送检率', )
    dvt_prevent = fields.Integer(u'深静脉血栓（DVT）预防率', )
    mortality = fields.Integer(u'ICU 患者实际病死率', )
    predict_mortality = fields.Integer(u'ICU 患者预计病死率', )
    std_mortality = fields.Integer(u'ICU 症患者标化病死指数', )
    unplanned_extubation = fields.Integer(u'非计划气管插管拔管率', )
    intubation_within48h = fields.Integer(u'气管插管拔管后48h内再插管率', )
    return_within48h = fields.Integer(u'转出ICU后48h内重返率', )
    vpa_rate = fields.Integer(u'呼吸机相关性肺炎（VAP）发病率', )
    crbsi_rate = fields.Integer(u'血管内导管相关血流感染（CRBSI）发病率', )
    cauti_rate = fields.Integer(u'导尿管相关泌尿系感染（CAUTI）发病率', )
