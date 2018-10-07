function menu() {
    var x=document.getElementById("menu");
    if(x.className==="menu"){
        x.classList.toggle("change");
        document.getElementById("web").id="webout";
        opennav();}
    else{
        x.classList.toggle("change");
        document.getElementById("webout").id="web";
        closenav();
    }
}
function opennav() {
    document.getElementById("sidenav").style.width = "250px";
    document.getElementById("main").style.marginRight = "250px";
}
function closenav() {
    document.getElementById("sidenav").style.width = "0";
    document.getElementById("main").style.marginRight = "0";
}
window.onscroll = function() {scroll()};
function scroll() {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        document.getElementById("topbtn").style.opacity = "1";
    } else {
        document.getElementById("topbtn").style.opacity= "0";
    }
    if(document.body.scrollTop > 2200 || document.documentElement.scrollTop > 2200){
        document.getElementById("1").style.marginLeft="2%";
        document.getElementById("1").style.opacity="1";
        document.getElementById("2").style.marginLeft="2%";
        document.getElementById("2").style.opacity="1";
    }
    if(document.body.scrollTop > 2900 || document.documentElement.scrollTop > 2900){
        document.getElementById("3").style.marginTop="0";
        document.getElementById("3").style.opacity="1";
    }
    if(document.body.scrollTop > 3350 || document.documentElement.scrollTop > 3350){
        document.getElementById("4").style.marginLeft="2%";
        document.getElementById("4").style.opacity="1";
        document.getElementById("5").style.marginLeft="2%";
        document.getElementById("5").style.opacity="1";
    }
    if(document.body.scrollTop > 4000 || document.documentElement.scrollTop > 4000){
        document.getElementById("6").style.marginTop="0";
        document.getElementById("6").style.opacity="1";
    }
    if(document.body.scrollTop > 4450 || document.documentElement.scrollTop > 4450){
        document.getElementById("7").style.marginLeft="2%";
        document.getElementById("7").style.opacity="1";
        document.getElementById("8").style.marginLeft="2%";
        document.getElementById("8").style.opacity="1";
    }
}
function topbtn() {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200)
    $('body,html').animate({scrollTop:0},500);
}