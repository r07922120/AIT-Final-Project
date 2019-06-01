document.getElementById("video").style.width = "100px"

document.addEventListener('keydown', distance);
function distance(event) {
    if(event.keyCode == 87){
        console.log('up');

        width = $("video").width() + 50 + "px";
        document.getElementById("video").style.width = width;

    }else if(event.keyCode == 83){
        console.log('down');

        width = $("video").width() - 50 + "px";
        document.getElementById("video").style.width = width; 
    }
}