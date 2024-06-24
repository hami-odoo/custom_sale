from odoo import models, fields

class CustomProductPricelist(models.Model):
    """
        Custom ProductPricelist model
    """
    _inherit = "product.pricelist"
    _description = "Custom Price List"

    def show_pricelist_product_view(self):
        """Button action to display tree view for products having current pricelist applied.s

        Returns:
            dict: View to display products inside pricelist in Tree View. 
        """

        domain = [('id', 'in', self.item_ids.ids)]
        data =  {
            'name': self.display_name,
            'view_type': 'tree',
            'view_mode': 'tree',
            'res_model': 'product.pricelist.item',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': domain
        }
        return data