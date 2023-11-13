var dark = 0;

var navbar = document.getElementsByClassName("navbutton");
var about = document.getElementsByClassName("about");
var body = document.getElementsByTagName("body");
var html = document.getElementsByTagName("html");

photo = document.getElementsByClassName("p1");

var h1 = document.getElementsByTagName("h1");
var h2 = document.getElementsByTagName("h2");
var h6 = document.getElementsByTagName("h6");
var h4 = document.getElementsByTagName("h4");

var p = document.getElementsByTagName("p");

function light_mode(){
  document.getElementById("switch").innerHTML = "🌙";
  document.getElementById("switch").title = "Dark Mode";
  try{
    photo[0].src = "static/images/photo_light.png";
    photo[0].style.borderTop = "solid white 60px";
  }
  catch {}
  for (var i = 0; i < navbar.length; i++) navbar[i].style.color = "black";
  for (var i = 0; i < body.length; i++) body[i].style.backgroundColor = "white";
  for (var i = 0; i < html.length; i++) html[i].style.backgroundColor = "white";
  for (var i = 0; i < about.length; i++) about[i].style.backgroundColor = "white";
  for (var i = 0; i < h1.length; i++) h1[i].style.color = "black";
  for (var i = 0; i < h2.length; i++) h2[i].style.color = "black";
  for (var i = 0; i < h4.length; i++) h4[i].style.color = "black";
  for (var i = 0; i < h6.length; i++) h6[i].style.color = "black";
  for (var i = 0; i < p.length; i++) p[i].style.color = "black";
}

function dark_mode(){
  document.getElementById("switch").innerHTML = "⛅";
  document.getElementById("switch").title = "Light Mode";
  try{
    photo[0].src = "static/images/photo.png";
    photo[0].style.borderTop = "solid black 60px";
  }
  catch {}
  for (var i = 0; i < navbar.length; i++) navbar[i].style.color = "white";
  for (var i = 0; i < body.length; i++) body[i].style.backgroundColor = "black";
  for (var i = 0; i < html.length; i++) html[i].style.backgroundColor = "black";
  for (var i = 0; i < about.length; i++) about[i].style.backgroundColor = "black";
  for (var i = 0; i < h1.length; i++) h1[i].style.color = "white";
  for (var i = 0; i < h2.length; i++) h2[i].style.color = "white";
  for (var i = 0; i < h4.length; i++) h4[i].style.color = "white";
  for (var i = 0; i < h6.length; i++) h6[i].style.color = "white";
  for (var i = 0; i < p.length; i++) p[i].style.color = "white";
}

function mode_shift(){
  console.log(dark);
  dark ++;
  if (dark % 2 == 1) {
    light_mode();
    console.log("Dark");
  }
  else {
    dark_mode();
    console.log("light");
  }
  // console.log(dark);
}