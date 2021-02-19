# -*- coding: utf-8 -*-
# Copyright (c) 2016 Amzsys IT Solutions Pvt Ltd
# (http://www.amzsys.com)
# info@amzsys.com
# - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CallTracking(models.Model):
    _name = "call.tracking"
    _rec_name = 'next_activity_id'

    opportunity_id = fields.Many2one(
        comodel_name="crm.lead", string="Opportunity")
    next_activity_id = fields.Many2one(
        comodel_name="mail.activity.type", string="Next Activity")
    date_action = fields.Date('Activity Date')
    title_action = fields.Char('Activity Summary')
