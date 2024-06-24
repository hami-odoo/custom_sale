from odoo import models, fields
from odoo.exceptions import ValidationError

class CustomPurchaseOrder(models.Model):
    """
        Custom PurchaseOrder model
    """
    _inherit = "purchase.order"

    def _get_po_so_orderlines(self, rec):
        return {pol.product_id.id: pol for pol in rec.order_line}, {sol.product_id.id: sol for sol in rec.auto_sale_order_id.order_line}

    def update_price(self):    
        """
        Button action to update price on PO from correspoding SO. - Multicompany Rules
        Args:
            self: purchase.order

        Returns:
            _value: True
            _type: boolean
        """
        for rec in self:
            product_purchase_order_line_dict, product_sale_order_line_dict = self._get_po_so_orderlines(rec=rec)

            for product_id in product_purchase_order_line_dict.keys():
                if product_id in product_sale_order_line_dict:
                    product_purchase_order_line_dict[product_id].price_unit = product_sale_order_line_dict[product_id].price_unit

        return True
    
    def button_confirm(self):
        """Validation to check if prices are same on both SO and PO.

        Raises:
            ValidationError: Prices may not be updated.

        Returns:
            function call to confirm PO.
        """
        for rec in self:
            product_purchase_order_line_dict, product_sale_order_line_dict = self._get_po_so_orderlines(rec=rec)

            for product_id in product_purchase_order_line_dict.keys():
                if product_id in product_sale_order_line_dict:
                    if product_purchase_order_line_dict[product_id].price_unit != product_sale_order_line_dict[product_id].price_unit:
                        raise ValidationError("Some Order's price may not be updated. Kindly Update them before confirming.")

        return super().button_confirm()
    