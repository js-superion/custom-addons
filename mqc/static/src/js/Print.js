/**
 * Created by Administrator on 2016-07-28.
 */
odoo.define('', function (require) {

    'use strict';

    var ajax = require('web.ajax');
    var core = require('web.core');
    var form_widgets = require('web.form_widgets');

    var LODOP; var printMdl;
    var lodop = function () {
        if (LODOP == null) {
            LODOP = getLodop(document.getElementById('LODOP_OB'), document.getElementById('LODOP_EM'));
        }
        return LODOP;
    }

    var PrintButton = form_widgets.WidgetButton.extend({
        on_click: function () {
            var LODOP = lodop();
            var model = this.view.model;
            var key = '';
            if (this.node.attrs.model) model = this.node.attrs.model;
            if (this.node.attrs.key) key = this.node.attrs.key;
            if (printMdl == undefined) {
                printgetmdl(model, key, function (data) {
                    printMdl = data;
                    eval(printMdl);
                    LODOP.PREVIEW();
                });
            } else {
                eval(printMdl);
                LODOP.PREVIEW();
            }
        }
    });
    
     core.form_tag_registry.add('printbutton', PrintButton);

})
