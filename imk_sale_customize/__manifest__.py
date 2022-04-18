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
        'views/sale_view.xml',
        'views/purchase_view.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    'installable': True,
    'application': True,
    'auto_install': True,
}
