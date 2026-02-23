const socket = io();

function type(msg){

let term =
document.getElementById("terminal");

let i=0;

let interval=setInterval(()=>{

term.innerHTML+=msg[i];
i++;

if(i>=msg.length){
term.innerHTML+="<br>";
clearInterval(interval);
}

term.scrollTop=term.scrollHeight;

},5);
}

function startScan(){

document.getElementById(
"terminal").innerHTML="";

let target=
document.getElementById("target").value;

socket.emit("start_scan",
{target:target});
}

socket.on("update",(msg)=>{
type(msg);
});
