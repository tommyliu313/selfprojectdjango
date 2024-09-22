function openeye(){
    var valueofpassword = document.getElementById("password");
    if(valueofpassword.type === "password"){
        valueofpassword.type= "text";
    }
    else{
        valueofpassword.type= "password";
    }
}