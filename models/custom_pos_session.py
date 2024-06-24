from odoo import models

class CustomPosSession(models.Model):
    _inherit="pos.session"

    def _loader_params_product_product(self):   
        return {
            'search_params': {
                'domain': self.config_id._get_available_product_domain(),
                'fields': [
                    'display_name', 'lst_price', 'standard_price', 'categ_id', 'pos_categ_ids', 'taxes_id', 'barcode',
                    'default_code', 'to_weight', 'uom_id', 'description_sale', 'description', 'product_tmpl_id', 'tracking',
                    'write_date', 'available_in_pos', 'attribute_line_ids', 'active', 'image_128', 'combo_ids', 'hide_variant'
                ],
                'order': 'sequence,default_code,name',
            },
            'context': {'display_default_code': False},
        }


