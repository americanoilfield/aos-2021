# -*- coding: utf-8 -*-
# Copyright (c) 2016 Amzsys IT Solutions Pvt Ltd
# (http://www.amzsys.com)
# info@amzsys.com
# - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    number = fields.Char('Number', size=64, readonly=True)
    tracking_ids = fields.One2many(
        comodel_name='call.tracking',
        inverse_name='opportunity_id',
        string='Tracking')

    @api.model
    def create(self, vals):
        SequenceObj = self.env['ir.sequence']
        vals['number'] = SequenceObj.next_by_code('crm.lead')
        return super(CrmLead, self).create(vals)
