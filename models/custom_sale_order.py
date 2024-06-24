from odoo import models, fields
from odoo.exceptions import ValidationError

class CustomSaleOrder(models.Model):
    """
        Custom SaleOrder model
    """
    
    _inherit = "sale.order"
    _description = ""

    employee_id = fields.Many2one('hr.employee', string="Employee")

    def _get_po_so_orderlines(self, rec):
        return {pol.product_id.id: pol for pol in rec.auto_purchase_order_id.order_line}, {sol.product_id.id: sol for sol in rec.order_line}

    
    def update_price(self):
        """
        Button action to update price on SO from correspoding PO. - Multicompany Rules.
        Args:
            self: sale.order

        Returns:
            _value: True
            _type: boolean
        """

        for rec in self:
            product_purchase_order_line_dict, product_sale_order_line_dict = self._get_po_so_orderlines(rec=rec)
            
            for product_id in product_purchase_order_line_dict.keys():
                if product_id in product_sale_order_line_dict:
                    product_sale_order_line_dict[product_id].price_unit = product_purchase_order_line_dict[product_id].price_total

        return True
    
    def action_confirm(self):
        """Validation to check if prices are same on both SO and PO.

        Raises:
            ValidationError: Prices may not be updated.

        Returns:
            function call to confirm SO.
        """
        
        for rec in self:
            product_purchase_order_line_dict, product_sale_order_line_dict = self._get_po_so_orderlines(rec=rec)
            
            for product_id in product_purchase_order_line_dict.keys():
                if product_id in product_sale_order_line_dict:
                    if product_sale_order_line_dict[product_id].price_unit != product_purchase_order_line_dict[product_id].price_total:
                        raise ValidationError("Some Order's price may not be updated. Kindly Update them before confirming.")

        return super().action_confirm()