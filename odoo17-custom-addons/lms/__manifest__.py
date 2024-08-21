# -*- coding: utf-8 -*-
{
    'name': "lms",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "UIC LMS ",
    'website': "exmple.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        
        # security
        'security/security.xml',
        'security/ir.model.access.csv',
        # data

        # views
        'views/menu.xml',
        'views/teachers.xml',
        'views/payments.xml',
        'views/others.xml',
        'views/teacher_payments.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    "application": True,
    "installable": True,
}

