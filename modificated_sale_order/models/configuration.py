
from odoo import models, fields, api

class ConfigurationValidation(models.Model):
    _name = 'sale.custom.config'
    _description = 'Modificated Sale Order for Technical Test'
    
    name = fields.Char(string="Name")
    state = fields.Boolean(string="State")
    