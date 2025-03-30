odoo.define('modificated_payscreen.Generate_code_operation', function (require) {
    "use strict";

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

    class CustomCodeOperation extends PosComponent {
        get generateOperationCode() {
            let codeOperationModificated = document.getElementById("code-operation-modificated");
            if (codeOperationModificated) {
                return codeOperationModificated.textContent;
            } else {
                let letters = 'OP-' + crypto.randomUUID().split('-')[0].toUpperCase();
                return letters
            }
        }
        
    }
    CustomCodeOperation.template = "CodeOperation";

    Registries.Component.add(CustomCodeOperation);

    return CustomCodeOperation;
});