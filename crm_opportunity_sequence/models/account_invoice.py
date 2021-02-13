# -*- coding: utf-8 -*-
# Copyright (c) 2016 Amzsys IT Solutions Pvt Ltd
# (http://www.amzsys.com)
# info@amzsys.com
# - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class account_invoice(models.Model):
    _inherit = "account.invoice"

    opp_ref = fields.Char('Opportunity Reference', readonly=True)
