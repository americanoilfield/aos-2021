# -*- coding: utf-8 -*-


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
        vals['name'] = "{} {}".format(vals['number'], vals['name'])
        return super(CrmLead, self).create(vals)
