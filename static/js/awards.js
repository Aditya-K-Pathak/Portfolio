document.onreadystatechange = function () {
    if (document.readyState !== "complete") {
       document.querySelector("body").style.visibility = "hidden";
       document.getElementById("loading_indicator").style.visibility = "visible";
    }
    else{
       document.getElementById("loading_indicator").style.display ="none";
       document.querySelector("body").style.visibility = "visible";
    }
 };
 
 $(document).ready(()=>{
     if (!window.localStorage.getItem('ip_address')){
     $.getJSON("https://api.ipify.org?format=json",
     function (data) {
         console.log(data.ip)
         document.getElementById('id_ip_address').value=data.ip;
         document.getElementById('submit_weather').click();
         window.localStorage.setItem('ip_address', data.ip);
     })}
     else document.getElementById('ip_form').innerHTML=''
 });

 