const socket=io();

function type(text){

let term=document.getElementById("terminal");

let i=0;

let inter=setInterval(()=>{

term.innerHTML+=text[i];
i++;

if(i>=text.length){
term.innerHTML+="<br>";
clearInterval(inter);
}

term.scrollTop=term.scrollHeight;

},3);
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
