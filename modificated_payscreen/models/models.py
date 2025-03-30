# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ModificatedPayscreen(models.Model):
    _inherit = 'pos.payment'
    _description = 'Add fields to the payment screen'
    
    number_operation = fields.Char(string="Number Operation")