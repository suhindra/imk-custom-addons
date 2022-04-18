{
    'name': 'IMK Custom Report',
    'version': '1.0',
    'depends': ['base', 'account', 'stock', 'sale'],
    'author': "Suhindra",
    'maintainer': 'Suhindra',
    'license': "AGPL-3",
    'summary': '''IMK Custom Report''',
    'data': [
            'report/account_invoice.xml',
            'views/stock_picking.xml',
            'views/account_invoice.xml',
            'report/stock_picking.xml',
            
    ],
    'installable': True,
    'auto_install': False,
}
