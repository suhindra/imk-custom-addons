# -*- coding: utf-8 -*-
{
    'name': '',
    'version': '12.01',
    'author': 'Suhindra',
    'category': 'Sales',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """    
    custom sales for imk
    """,
    'description': """
   custom sales
    """,
    'images': ['static/description/banner.gif'],
    'depends': [
        'base',
        'sale',
    ],
    'data': [
        'views/app_odoo_customize_views.xml',
        'views/app_theme_config_settings_views.xml',
        'views/ir_model_views.xml',
        'views/ir_views.xml',
        # data
        'data/ir_config_parameter.xml',
        'data/ir_module_module.xml',
        # 'data/digest_template_data.xml',
        'data/res_company_data.xml',
        'data/res_groups.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    'installable': True,
    'application': True,
    'auto_install': True,
}
