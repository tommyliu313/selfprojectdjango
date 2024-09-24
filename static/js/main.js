function openeye(){
    var valueofpassword = document.getElementById("password");
    if(valueofpassword.type === "password"){
        valueofpassword.type= "text";
    }
    else{
        valueofpassword.type= "password";
    }
}

$(window).scroll(function(e){
    if ($(window).scrollTop()>=100 && $(window).scrollTop() !=0){
       $("button.button.is-link.modal-button").removeClass("hidden");}
    else{
       $("button.button.is-link.modal-button").addClass("hidden");}
  });