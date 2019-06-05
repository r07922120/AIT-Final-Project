var video = $("video").get(0);
var preText = 0;

document.addEventListener('keydown', distance);
function distance(event) {
    if(event.keyCode == 107){
        console.log('far');

        // if(!video.paused){
        video.requestFullscreen();
        // }

    }else if(event.keyCode == 109){
        console.log('near');

        if (document.fullscreen) {
            // console.log('full')
            document.exitFullscreen();
        }
    }
}

function readTextFile()
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", 'output.txt');
    // console.log(rawFile)
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                console.log(allText)
                if(preText != allText){
                    preText = allText;
                    if(allText == 0){
                        console.log('near');

                        if (document.fullscreen) {
                            // console.log('full')
                            document.exitFullscreen();
                        }
                
                    }else if(event.keyCode == 70 || allText == 1){
                        console.log('far');
                
                        // if(!video.paused){
                        video.requestFullscreen();
                        // }
                    }
                }
            }
        }
    }
    rawFile.send(null);
}

setInterval(readTextFile, 5);