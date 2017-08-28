var counter=0;

function loadCartValue(){

    var value=localStorage.getItem('cartItemCount')
    if(value){
        counter=value;
        document.getElementById("cart_count").innerHTML=value;
    }
    else{
        counter=0;
    }

    
}

document.addEventListener('DOMContentLoaded', function() {
    loadCartValue();
}, false);

function incrementCartCounter(){
    counter++;
    console.log(counter);
    localStorage.setItem('cartItemCount',counter);
    //setCookie("cartItemCount",counter,1)
    document.getElementById("cart_count").innerHTML=counter;
    
   
}


function decrementCartCounter(item_count){
    counter=counter-item_count;
    localStorage.setItem('cartItemCount',counter);
    document.getElementById("cart_count").innerHTML=counter;
   
}

$('.btn-add').click(function(){
    incrementCartCounter();        
});


