
function validateform() { 
	const us=document.getElementById("username").value;

    var pw = document.getElementById("password").value; 
    if(us == "") {
        document.getElementById("message1").innerHTML = "**Fill the username  please!";  
        return false;  
    }
    if(pw == "") {  
        document.getElementById("message").innerHTML = "**Fill the password please!";  
        return false;  
     } 

  

 
//minimum password length validation  
if(pw.length < 8) {  
   document.getElementById("message").innerHTML = "**Password length must be atleast 8 characters";  
   return false;  
}  

//maximum length of password validation  
if(pw.length > 15) {  
   document.getElementById("message").innerHTML = "**Password length must not exceed 15 characters";  
   return false;  
} else {  
   alert("you sign-up successfully");  
}  
}