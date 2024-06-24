//  @odoo-module /

import { OrderReceipt } from "@point_of_sale/app/screens/receipt_screen/receipt/order_receipt";
import { patch } from "@web/core/utils/patch";

patch(OrderReceipt.prototype, {

    getDisplayDataForReceipt(args) {
        if (args.hide_variant){
            args.productName = args.productName.replace(new RegExp('\\(.*\\)'),"").trim()
       }
        return this.omit(args, 'customerNote')
    }

});