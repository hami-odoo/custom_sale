from odoo import models, fields
import re

class CustomProduct(models.Model):
    """
        Custom ProductTemplate model
    """
    
    _inherit = 'product.template'
    _description = 'Class for customization on Product Form'

    hide_variant = fields.Boolean(string='Hide Product Variant') # when set hides the variant name from the SO and POS Bill.

    def hide_variant_name(self, text):
        """
        Substitutes the (variant name) with '' inside the product name. 

        Args:
            text (string): variant name

        Returns:
            string : description with variant name remove.
        """
        return re.sub('\(.*\)', '', text)

        