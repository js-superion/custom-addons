odoo.define('lodop.print', function(require){
    'use strict';

    var ajax=require('web.ajax');
    var core = require('web.core');
    var form_widgets = require('web.form_widgets');

    var LODOP;
    var printMdl;
    var lodop= function(){
        if(LODOP==null){
            LODOP=getLodop(document.getElementById('LODOP_OB'), document.getElementById('LODOP_EM'));
        }
        return LODOP;
    }

    var printgetmdl = function(model, key, ref){
        ajax.post('/print/template/get', {'model': model, 'key': key})
            .then(function(data){
                ref(data,model,key);
            });
    }

    var printsetmdl = function(model, key, template){
        var rst;
        ajax.post('/print/template/set', {'model': model, 'key': key, 'template': template});
    }

    var printgetrst = function(model, key, ids, pieces, ref){
        ajax.post('/print/get', {'model': model, 'key': key, 'ids': ids, 'pieces': pieces})
            .then(function(data){
                ref(data,model,key);
            })
    }

    var printcnt = function(model, ids){
        ajax.post('/print/count', {'model': model, 'ids': ids})
    }

    function lodopDesign(printMdl, model, key){
        LODOP.SET_SHOW_MODE("DESIGN_IN_BROWSE",1);
        if(printMdl){
            eval(printMdl);
        }

        if (LODOP.CVERSION && !LODOP.On_Return) {
            LODOP.On_Return = function (TaskID, Value) {
                if (Value != "" && Value!="NoResult") {
                    printMdl = Value;
                    printsetmdl(model, key, printMdl);
                };
            }
        }
        LODOP.PRINT_DESIGN();
    }


    var PrintButton = form_widgets.WidgetButton.extend({
        init:function(parent, options){
            this._super.apply(this,arguments),
            this.htmlfrom = "client"
        },
        on_click: function() {
            var LODOP = lodop();
            var model=this.view.model;
            var key = '';
            var htmlfrom = '';
            var html='';
            if(this.node.attrs.htmlfrom) htmlfrom = this.node.attrs.htmlfrom;
            if(htmlfrom=='' || htmlfrom=='client'){
                 html = $("#blood_form").html();
                var width = $("#blood_form").width();
                var height = $("#blood_form").height();
                 LODOP.ADD_PRINT_TABLE(88,40,width,height,html);
            }else{
                if(this.node.attrs.model) model=this.node.attrs.model;
                if(this.node.attrs.key) key=this.node.attrs.key;
                printgetmdl(model, key, function (data) {
                    if(!data){
                        html = $("#blood_form").html();
                        LODOP.ADD_PRINT_HTM(88,40,321,185,html);
                    }else{
                         printMdl = data;
                        eval(printMdl);
                    }
                });
            }
             //execute html tab or js script
            LODOP.PREVIEW();
        }
    });

    core.form_tag_registry.add('printbutton', PrintButton);

    var PrintDesignButton = form_widgets.WidgetButton.extend({
        on_click: function(){
            var LODOP=lodop();
            var model=this.view.model;
            var key='';
            if(this.node.attrs.model) model=this.node.attrs.model;
            if(this.node.attrs.key) key=this.node.attrs.key;
            // if(printMdl==undefined){
                printgetmdl(model,key,function(data,model,key){
                    lodopDesign(data,model,key);
                })
            // }else{
            //     lodopDesign(printMdl,this.view.model,key);
            // }
        }
    })

    core.form_tag_registry.add('printdesignbutton', PrintDesignButton);

    return {
        lodop: lodop,
        printgetmdl:printgetmdl,
        printgetrst:printgetrst,
        printcnt:printcnt,
    };
})