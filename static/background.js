const canvas=document.getElementById("bg");
const ctx=canvas.getContext("2d");

canvas.width=window.innerWidth;
canvas.height=window.innerHeight;

function draw(){

ctx.fillStyle="rgba(0,10,20,0.2)";
ctx.fillRect(0,0,
canvas.width,
canvas.height);

ctx.strokeStyle="#00f7ff22";

for(let i=0;i<canvas.width;i+=50){
ctx.beginPath();
ctx.moveTo(i,0);
ctx.lineTo(i,canvas.height);
ctx.stroke();
}

for(let j=0;j<canvas.height;j+=50){
ctx.beginPath();
ctx.moveTo(0,j);
ctx.lineTo(canvas.width,j);
ctx.stroke();
}
}

setInterval(draw,60);
