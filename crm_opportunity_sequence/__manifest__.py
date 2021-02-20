# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2016 Amzsys IT Solutions Pvt Ltd
#    (http://www.amzsys.com)
#    info@amzsys.com
#    Manuel Marquez <buzondemam@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Opportunity',
    'version': '1.0',
    'category': 'CRM Opportunity customization',
    'description': """
        Call log Tracking Customization
    """,
    'author': 'Amzsys',
    'website': 'http://www.amzsys.com/',
    'summary': '',
    'depends': [
        'sales_team', 'crm', 'sale', 'sale_crm', 'account'
    ],
    'data': [
        'security/crm_security.xml',
        'security/ir.model.access.csv',
        'data/opportunity_sequence.xml',
        'views/crm_lead_views.xml',
        'views/account_move_views.xml',
        'views/sale_order_views.xml',
        'views/call_tracking_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
