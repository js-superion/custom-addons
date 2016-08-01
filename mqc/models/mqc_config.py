# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.exceptions import ValidationError


class ConfigHospital(models.Model):
    _name = "mqc.hospital"
    _inherits = {'res.partner':'partner_id'}
    #关联到res_partner，级联删除
    partner_id = fields.Many2one(
        'res.partner',
        u'医院名称',
        ondelete ='cascade')
    hospital_code = fields.Char(
        u'平台编码',
        require=True,
    )

    @api.one
    @api.constrains('partner_id')
    def _check_hospital_id(self):
        domain = [
            ('partner_id', '=', self.partner_id),
        ]
        if len(self.search(domain)) > 1:
            raise ValidationError(u'医院名称不能重复')

    @api.one
    @api.constrains('hospital_code')
    def _check_hospital_code(self):
        domain = [
            ('hospital_code', '=', self.hospital_code),
        ]
        if len(self.search(domain)) > 1:
            raise ValidationError(u'医院编码不能重复')


class ConfigUser(models.Model):
    _name = "mqc.user"
    _inherits = {'res.partner':'user_id'}
    #关联到res_partner，级联删除
    user_id = fields.Many2one(
        'res.partner',
        u'用户名称的',
        ondelete ='cascade')
    user_code = fields.Char(
        u'平台编码',
        require=True,
    )

    @api.one
    @api.constrains('user_id')
    def _check_user_id(self):
        domain = [
            ('user_id', '=', self.user_id),
        ]
        if len(self.search(domain)) > 1:
            raise ValidationError(u'用户名称不能重复')

    @api.one
    @api.constrains('user_code')
    def _check_user_code(self):
        domain = [
            ('user_code', '=', self.user_code),
        ]
        if len(self.search(domain)) > 1:
            raise ValidationError(u'用户编码不能重复')

