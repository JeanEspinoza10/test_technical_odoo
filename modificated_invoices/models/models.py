from odoo import models, fields, api


class ModificatedInvoices(models.Model):
    _inherit = 'account.move'
    
    '''
    The requested field is x_document_type, but I changed it to type_document for readability when writing the code.
    '''
    
    type_document = fields.Selection(
        [
            ('Boleta', 'Boleta'),
            ('Factura', 'Factura'),
        ],
        string="Type of Document",
        default='Boleta',
        required=True
    )
    user_has_group = fields.Boolean(compute="_compute_user_group")

    @api.depends_context('uid')
    def _compute_user_group(self):
        for record in self:
            record.user_has_group = self.env.user.has_group('modificated_invoices.group_modificated_invoices_admin')
    