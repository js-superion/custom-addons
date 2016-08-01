# -*- coding: utf-8 -*-
{
    'name': "mqc",

    'summary': """
        Medical Quality Control
        医疗质量控制信息上报模块""",

    'description': """
        包含以下学科：ICU，急诊，病理，护理，口腔，临床，麻醉，血透，药事，影像，院感
    """,

    'author': "江苏正融科技",
    'website': "http://www.superion.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'mqc',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'security/emerg_security.xml',
        'views/mqc_emerg.xml',
        'views/mqc_blood.xml',
        'views/mqc_cfg.xml',
        'views/mqc_menuitem.xml',
        'views/blood_form_view.xml',
        'report/mqc_emrg_report_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}