function openTips(){
  var tips = document.getElementById("tips");
  tips.style.display = "block";
}
document.getElementById("tips").style.display ="none";
setTimeout("openTips()", 900000);