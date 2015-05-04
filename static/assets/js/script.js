$(document).ready(function() {
    $("#id_1-place").geocomplete()
          .bind("geocode:result", function(event, result){
          })
    //Omitimos los enlaces sin destino
    $('a[href="#"]').click(function(event) {
        event.preventDefault();
    });

    //Activamos los tooltip de la lib javascript de bootstrap
    $('[data-toggle="tooltip"]').tooltip()
    //$(function () {
    //})
    
    //Popup
    /*
    //open popup
    $('.cd-popup-trigger').on('click', function(event){
        event.preventDefault();
        $('.cd-popup').addClass('is-visible');
    });
    
    //close popup
    $('.cd-popup').on('click', function(event){
        if( $(event.target).is('.cd-popup-close') || $(event.target).is('.cd-popup') ) {
            event.preventDefault();
            $(this).removeClass('is-visible');
        }
    });
    //close popup when clicking the esc keyboard button
    $(document).keyup(function(event){
        if(event.which=='27'){
            $('.cd-popup').removeClass('is-visible');
        }
    });

    $('#drop a').click(function(){
        // Simulate a click on the file input button
        // to show the file browser dialog
        $(this).parent().find('input').click();
    });*/
    function LoadSubCategory(category, assing_category) {

        $("#subcategoria").removeClass("hide");
        var HTML = '<select id="id_0-subcategory" name="0-subcategory"><option value="" selected="selected">---------</option></select>';
        $("#subcategoria div").html(HTML);

        $.ajax({
            url: '/ajax_load_subcategory/',
            data: {'term':category},
            type: 'get',
            success: function(data) {
                
                var HTML;
                for (var i = 0, len = data.length; i < len; ++i) {
                    HTML += '<option value="' + data[i]['id'] + '">' + data[i]['name'] + '</option>';
                } 
                $('#id_0-subcategory').append(HTML);

                if (assing_category) {
                    $('#id_0-subcategory').val(assing_category);
                }
            },
        });
        
    }

    function LoadCategory(argument) {
        $.ajax({
            url: '/ajax_load_category_from_autocomplete_company/',
            data: {'term':argument},
            type: 'get',
            success: function(data) {
               //console.log("LoadCategory: ", data);
               $('#id_0-category').val(data.category);
               LoadSubCategory(data.category, data.subcategory);
            },
        }); 
    }
    
    $('#id_0-company').keyup(function() {
         if(!$.trim(this.value).length) {
            $('#id_0-company_val').val("");
            $('#id_0-category').val($("#id_0-category option:first").val());
            $("#subcategoria div").html("");
            $("#subcategoria").addClass("hide");
            $(".ui-autocomplete-empty-message").empty();
            $(".ui-autocomplete-empty-message").removeClass('show');
         }
    });

    $('#id_0-category').change(function(event) {
        event.preventDefault();
        var option = $(this).val();
        LoadSubCategory(option);
        console.log("LoadCategory: ",option);
    });

    $("#id_0-company").autocomplete({
        source     : "/ajax_company/",
        dataType   : "json",
        selectFirst: true,
        autoFocus  : true,
        minLength  : 2,
        response: function(event, ui) {
            if (ui.content.length === 0) {
                $('#id_0-company_val').val("");
                $('#id_0-category').val($("#id_0-category option:first").val());
                $("#subcategoria div").html("");
                $("#subcategoria").addClass("hide");

                $(".ui-autocomplete-empty-message").addClass('show');
                $(".ui-autocomplete-empty-message").html("Esta empresa no se encuentra en nuestra base de datos, <strong>Si continua se agregara automaticamente</strong>");
            } else {
                $(".ui-autocomplete-empty-message").empty();
                $(".ui-autocomplete-empty-message").removeClass('show');
            }
        },
        select: function(event,ui) {
            var GOBAL_ID_COMPANY = ui.item.id;
            $('#id_0-company_val').val(GOBAL_ID_COMPANY);

            LoadCategory(GOBAL_ID_COMPANY);
        },
        //search     : function(){$(this).addClass('ui-autocomplete-loading');},
        //open       : function(){$(this).removeClass('ui-autocomplete-loading');},
    }).data("ui-autocomplete")._renderItem = function( ul, item ) {
        var inner_html = '<a><div class="list_item_container"><div class="image"><img src="' + item.image + '"></div><strong>' + item.label + '</strong><div class="description">' + item.description + '</div></div></a>';
        return $( "<li></li>" )
            .data( "item.autocomplete", item )
            .append(inner_html)
            .appendTo( ul );
    };

});