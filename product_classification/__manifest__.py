# -*- coding: utf-8 -*-
{
    'name': "product_classification",
    'summary': """
        Product Classification""",
    'description': """
        Fields for the classification of the product.
    """,
    'author': "gflores",
    'website': "https://www.gruporequiez.com",
    'category': 'Inventory',
    'version': '0.0.1',
    'license': "LGPL-3",
    'depends': ['product', 'stock', 'stock_account'],
    'data': [
        # views
        'views/product_template_view.xml',
        'views/stock_move_line_view.xml',
        'views/stock_valuation_layer_view.xml',
        # reports
    ],
    'demo': [
    ],
    'application': True,
}
