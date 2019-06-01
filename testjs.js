$(document).ready(function () {
    var isFull = false;
    $("span").click(function(){
        var cName = $(this).attr("class");
        var video = $("video").get(0);
        // console.log(video)
        if(cName == "far"){
            textFontSize = 24
            if(!video.paused){
                video.requestFullscreen();
                isFull = true;
            }
        }else if(cName == "near"){
            textFontSize = 14
            console.log(isFull)
            console.log(document.fullscreen)
            if (isFull && document.fullscreen) {
                console.log('full')
                video.exitFullscreen();
            }
        }
        $("body").css("font-size", textFontSize);
    });
});