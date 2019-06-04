document.getElementById("word").style.fontSize = "8px"

document.addEventListener('keydown', distance);
function distance(event) {
    if(event.keyCode == 87 || event.keyCode == 38){
        console.log('up');

        fontSize = document.getElementById("word").style.fontSize
        fontSize = fontSize.substr(0 , fontSize.length -2 )
        // console.log(fontSize)
        size = parseInt(fontSize) + 2 + "px";
        document.getElementById("word").style.fontSize = size;

    }else if(event.keyCode == 83 || event.keyCode == 40){
        console.log('down');

        fontSize = document.getElementById("word").style.fontSize
        fontSize = fontSize.substr(0 , fontSize.length -2 )

        size = parseInt(fontSize) - 2;
        if(size < 0){
            size = 0;
        }
        size = size + "px";
        document.getElementById("word").style.fontSize = size; 
    }else if(event.keyCode == 13){
        fontSize = document.getElementById("word").style.fontSize
        console.log(fontSize)
    }
}