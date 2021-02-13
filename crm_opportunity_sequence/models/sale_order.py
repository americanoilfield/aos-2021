# -*- coding: utf-8 -*-
# Copyright (c) 2016 Amzsys IT Solutions Pvt Ltd
# (http://www.amzsys.com)
# info@amzsys.com
# - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class sale_order(models.Model):
    _inherit = "sale.order"

    opp_ref = fields.Char('Opportunity Reference', readonly=True)

    @api.multi
    def _prepare_invoice(self):
        res = super(sale_order, self)._prepare_invoice()
        for order in self:
            if order.opp_ref:
                res['opp_ref'] = order.opp_ref
        return res
