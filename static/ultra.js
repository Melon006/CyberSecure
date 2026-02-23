const socket = io();

function startScan(){

let target =
document.getElementById("target").value;

document.getElementById(
"terminal").innerHTML="";

socket.emit("start_scan",
{target:target});
}

socket.on("update",(msg)=>{

let term =
document.getElementById("terminal");

term.innerHTML += msg + "<br>";
term.scrollTop = term.scrollHeight;

});
