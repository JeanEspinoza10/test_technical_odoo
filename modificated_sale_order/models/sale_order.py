
from odoo import models, fields, api
from odoo.exceptions import UserError

class ModificatedSaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Modificated Sale Order for Technical Test'

    def validate_quantity(self):
        for order in self:
            for line in order.order_line:
                product = line.product_id
                qty_required = line.product_uom_qty
                stock_available = product.virtual_available  
                if stock_available < qty_required:
                    raise UserError(
                        f"El producto {product.name} no tiene suficiente stock."
                    )
                    
    def action_confirm(self):
        is_active_validate_quantity = self.env['sale.custom.config'].search([('name', '=', 'Validación de Stock')])
        if is_active_validate_quantity.state:
            self.validate_quantity()
            
        return super(ModificatedSaleOrder, self).action_confirm()