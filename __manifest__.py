# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

{
    'name': 'Merge Manufacturing Order',
    'version': '14.0.1.0',
    'sequence': 1,
    'category': 'Manufacturing',
    'description':
        """
        This Module add below functionality into odoo

        1.Merge Confirmed Manufacturing Orders.
        2.When you merge Manufacturing Orders, a merged Manufacturing Order is created as new and selected Manufacturing Orders are cancel.
        6.Note : You can't merge Manufacturing Order which are not in confirmed state or not from similar Bill of Material

merge Manufacturing Order
merge mrp
merge mo
merge mrp order 
merge work order
merge mrporder
merge Manufacturing


    """,
    'summary': 'odoo app allow to Merge  Manufacturing Order,merge mrp,merge Manufacturing Order,merge mrp order,merge mrporder,merge Manufacturing,merge mo',
    'depends': ['mrp'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/merge_mrp_view.xml',
        ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    # author and support Details =============#
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',    
    'maintainer': 'DevIntelle Consulting Service Pvt.Ltd', 
    'support': '',
    'price': 25.0,
    'currency':'EUR',
    #'live_test_url':'https://youtu.be/A5kEBboAh_k',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
