preText = 1
inPicture = ""

$('#diving').mouseenter(function(){
    inPicture = "diving"
});
$('#diving').mouseleave(function(){
    inPicture = ""
});

$('#romantic').mouseenter(function(){
    inPicture = "romantic"
});
$('#romantic').mouseleave(function(){
    inPicture = ""
});

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
                
                        window.location.assign("tripadvisor.html#" + inPicture);
                
                    }
                }
            }
        }
    }
    rawFile.send(null);
}

setInterval(readTextFile, 5);