odoo.define('modificated_payscreen.PaymentScreenCustom', function (require) {
    "use strict";

    var PaymentScreen = require('point_of_sale.PaymentScreen'); // Importar PaymentScreen
    var { useListener } = require("@web/core/utils/hooks");
    var { patch } = require("@web/core/utils/patch");

    patch(PaymentScreen.prototype, "modificated_payscreen.PaymentScreenCustom", {
        setup() {
            this._super.apply(this, arguments);
            useListener("validate-order", this.customValidateOrder);
        },

        async customValidateOrder() {
            let elementCodeOperation = document.getElementById("code-operation-modificated");
            let codeOperation = elementCodeOperation.textContent;
            await this.validateOrder(false);
            let listIds = [];
            while (true) {
                let proxyObject = this.env.pos.validated_orders_name_server_id_map;
                let keys = Reflect.ownKeys(proxyObject);
                
                if (keys.length > 0) {
                    keys.forEach(key => {
                        listIds.push(Reflect.get(proxyObject, key));
                    });
                    this.env.pos.validated_orders_name_server_id_map = {};
                    break;
                }
                await new Promise(resolve => setTimeout(resolve, 100));
            }            
            await this.rpc({
                model: 'pos.payment',
                method: 'write',
                args: [[listIds[0]], {number_operation: codeOperation}],
            })
        }
    });
});