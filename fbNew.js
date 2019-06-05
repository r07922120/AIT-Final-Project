$("#moreText").hide();
preText = 0;

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

                    var fbTextPos  = $('#fbText').offset().top - $(window).scrollTop()
                    console.log(fbTextPos)
                    var fbImgPos  = $('#fbImg').offset().top - $(window).scrollTop()
                    console.log(fbImgPos)
                    var fbVideoPos  = $('#fbVideo').offset().top - $(window).scrollTop()
                    console.log(fbVideoPos)

                    center = "fbText"
                    if(Math.abs(fbTextPos) > Math.abs(fbImgPos)){
                        center = "fbImg"
                    }
                    if(Math.abs(fbImgPos) > Math.abs(fbVideoPos)){
                        center = "fbVideo"
                    }
                    console.log(center)

                    if(allText == 1){
                        console.log('far');
                
                        if(center == "fbText"){
                            $("#more").hide();
                            $("#moreText").show();
                        }else if(center == "fbImg"){
                            window.location.assign("fbImageNew.html");
                        }else if(center == "fbVideo"){
                            video.requestFullscreen();
                        }
                    }else if(allText == 0){
                        if(center == "fbText"){
                            $("#more").show();
                            $("#moreText").hide();
                        }else if(center == "fbVideo"){
                            if (document.fullscreen) {
                                document.exitFullscreen();
                            }
                        }
                    }
                }
            }
        }
    }
    rawFile.send(null);
}

setInterval(readTextFile, 5);