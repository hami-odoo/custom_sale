{
    'name': 'Custom Sales',
    'version': '1.0',
    'category': 'Sales/Sales',
    'summary': 'Sales internal machinery',
    'description': """
        This module contains custom features of Sales Management.
    """,
    'depends': [
        'base',
        'sale_management',
        'purchase',
        'hr',
        'sale_purchase_inter_company_rules',
        'point_of_sale'
    ],
    'data': [
        'views/custom_product_views.xml',
        'views/custom_sale_order_views.xml',
        'views/custom_purchase_order_views.xml',
        'report/custom_sale_ir_actions_report_templates.xml',
        'views/custom_product_pricelist_views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'assets': {
    },
    'license': 'LGPL-3',
    "assets": {
         'point_of_sale._assets_pos': [
            'custom_sale/static/src/**/*',
        ],
    }
}