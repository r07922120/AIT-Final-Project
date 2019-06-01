preText = 0
inPicture = ""

$('#cozumel').mouseenter(function(){
    inPicture = "cozumel"
});
$('#cozumel').mouseleave(function(){
    inPicture = ""
});

$('#kohnangyuan').mouseenter(function(){
    inPicture = "kohnangyuan"
});
$('#kohnangyuan').mouseleave(function(){
    inPicture = ""
});

$('#denational').mouseenter(function(){
    inPicture = "denational"
});
$('#denational').mouseleave(function(){
    inPicture = ""
});

$('#tulamben').mouseenter(function(){
    inPicture = "tulamben"
});
$('#tulamben').mouseleave(function(){
    inPicture = ""
});

$('#westend').mouseenter(function(){
    inPicture = "westend"
});
$('#westend').mouseleave(function(){
    inPicture = ""
});

$('#dahab').mouseenter(function(){
    inPicture = "dahab"
});
$('#dahab').mouseleave(function(){
    inPicture = ""
});

$('#paris').mouseenter(function(){
    inPicture = "paris"
});
$('#paris').mouseleave(function(){
    inPicture = ""
});

$('#puertovallarta').mouseenter(function(){
    inPicture = "puertovallarta"
});
$('#puertovallarta').mouseleave(function(){
    inPicture = ""
});

$('#venice').mouseenter(function(){
    inPicture = "venice"
});
$('#venice').mouseleave(function(){
    inPicture = ""
});

$('#sunsetcruise').mouseenter(function(){
    inPicture = "sunsetcruise"
});
$('#sunsetcruise').mouseleave(function(){
    inPicture = ""
});

$('#oia').mouseenter(function(){
    inPicture = "oia"
});
$('#oia').mouseleave(function(){
    inPicture = ""
});

$('#prague').mouseenter(function(){
    inPicture = "prague"
});
$('#prague').mouseleave(function(){
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
                    if(allText == 1){
                        console.log('far');
                
                        window.location.assign("tripadvisorFar.html#" + inPicture);
                    }
                }
            }
        }
    }
    rawFile.send(null);
}

setInterval(readTextFile, 5);