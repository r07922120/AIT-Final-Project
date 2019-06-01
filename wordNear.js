preText = 0;
inPage = "";

$('#page1').mouseenter(function(){
    inPage = "page1"
});
$('#page1').mouseleave(function(){
    inPage = ""
});

$('#page2').mouseenter(function(){
    inPage = "page2"
});
$('#page2').mouseleave(function(){
    inPage = ""
});

$('#page3').mouseenter(function(){
    inPage = "page3"
});
$('#page3').mouseleave(function(){
    inPage = ""
});

$('#page4').mouseenter(function(){
    inPage = "page4"
});
$('#page4').mouseleave(function(){
    inPage = ""
});

$('#page5').mouseenter(function(){
    inPage = "page5"
});
$('#page5').mouseleave(function(){
    inPage = ""
});

$('#page6').mouseenter(function(){
    inPage = "page6"
});
$('#page6').mouseleave(function(){
    inPage = ""
});

$('#page7').mouseenter(function(){
    inPage = "page7"
});
$('#page7').mouseleave(function(){
    inPage = ""
});

$('#page8').mouseenter(function(){
    inPage = "page8"
});
$('#page8').mouseleave(function(){
    inPage = ""
});

$('#page9').mouseenter(function(){
    inPage = "page9"
});
$('#page9').mouseleave(function(){
    inPage = ""
});

$('#page10').mouseenter(function(){
    inPage = "page10"
});
$('#page10').mouseleave(function(){
    inPage = ""
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
                
                        window.location.assign("word.html#" + inPage);
                
                    }
                }
            }
        }
    }
    rawFile.send(null);
}

setInterval(readTextFile, 5);