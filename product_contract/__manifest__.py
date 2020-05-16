# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Product Contract',
    'version': '10.0.1.1.0',
    'category': 'Contract Management',
    'license': 'AGPL-3',
    'author': "LasLabs, "
              "Odoo Community Association (OCA)",
    'website': 'https://github.com/oca/contract',
    'depends': [
        'contract',
        'product',
        'sale',
    ],
    'data': [
        'views/product_template_view.xml',
    ],
    'installable': True,
    'application': False,
}
