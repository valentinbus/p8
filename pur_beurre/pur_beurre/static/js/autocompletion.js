$(document).ready(function(){ 
    console.log("ok")    
    $("#search_product_home").autocomplete({
        source: "openfoodfact/ajax_calls/search/",
        minLength: 2,
        open: function(){
            setTimeout(function () {
                $('.ui-autocomplete').css('z-index', 99);
            }, 0);
        }
    });
    $("#search_product_home2").autocomplete({
        source: "openfoodfact/ajax_calls/search/",
        minLength: 2,
        open: function(){
            setTimeout(function () {
                $('.ui-autocomplete').css('z-index', 99);
            }, 0);
        }
    });
});