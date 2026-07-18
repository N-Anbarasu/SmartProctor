setTimeout(function(){

    document.querySelectorAll(".flash-message").forEach(function(message){

        message.style.opacity="0";

        setTimeout(function(){

            message.remove();

        },300);

    });

},10000);