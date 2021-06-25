let link = document.getElementById("lin");
let linkTxt  = link.innerText;

link.addEventListener("click",function(){
window.open(linkTxt, "_blank");
})
