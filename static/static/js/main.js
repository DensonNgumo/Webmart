var counter;

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}


function incrementCartCounter(){
    counter++;
    document.getElementById("cart_count").innerHTML=counter;
    setCookie("cartItemCount",counter,1)
   
}

function loadCartValue(){
    var value=getCookie("cartItemCount");
    if(value!=""){
        counter=value;
        document.getElementById("cart_count").innerHTML=value;
    }
    else{
        counter=0;
    }
    
}


var ProductsPage = {
    init: function() {
        this.$container = $('.testContainer');
        this.render();
        this.bindEvents();
    },

    render: function() {

    },

    bindEvents: function() {
        $('.btn-add', this.$container).on('click', function(e) {
            e.preventDefault();

            var self = $(this);
            var url = $(this).attr('href');
            $.getJSON(url, function(result) {
                if (result.success) {
                    $('.btn-add', self).css({color:'red'});
                }
            });

            return false;
        });
    }
};

$(document).ready(function() {
    ProductsPage.init();
    
});