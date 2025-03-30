from odoo import models, fields, api
from num2words import num2words
from odoo.exceptions import Warning

class CurrencyConverter(models.Model):
    _name = 'currency.converter'
    _description = "Model that will save users' conversion requests"

    name = fields.Char()
    quantity = fields.Float(string="Quantity")
    type_currency = fields.Selection(
        [
            ('PEN', 'PEN')
        ],
        string="Type of currency",
        default='PEN',
    )
    conversion_format = fields.Text(
        string="Conversion Format",
        compute="_compute_conversion_format",
        store=True 
    )
    
    def transform_number_letters(self, number:float) -> str:
        part_int = int(number)
        part_float = str(round((number - part_int) * 100))
        letters_part_int = num2words(part_int, lang='es').capitalize()
        return letters_part_int, part_float
    
    @api.depends('quantity', 'type_currency')
    def _compute_conversion_format(self):
        for record in self:
            try:
                letter_part_int,  part_float = self.transform_number_letters(record.quantity)        
                record.conversion_format = f"Son: {letter_part_int} con {part_float}/100 PEN"
            except Exception as e:
                Warning(f"Error converting {record.quantity} to PEN: {e}")