// C:\Program Files (x86)\Google\Chrome\Application
// .\chrome --allow-file-access-from-files

var open = document.getElementById('open');
var file = document.getElementById('file');
var fileDiv = document.getElementById('fileDiv');
var isOpen = false;
var preText = 0;

function clickMenu(){
    console.log('clickMenu')
    if(open.width != 0){
        $("#open").css("width", "0%");
        $("#fileDiv").css("width", "97%");
        file.setAttribute("src", "img/file.JPG");   
    }else{
        $("#open").css("width", "17%");
        $("#fileDiv").css("width", "80%");
        file.setAttribute("src", "img/fileOpen.JPG");   
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
                
                        $("#text").css("font-size", "18px");
                
                        if(isOpen){
                            $("#open").css("width", "17%");
                        }
                        isOpen = false;
                
                    }else if(allText == 1){
                        console.log('far');
                
                        $("#text").css("font-size", "24px");
                
                        if(open.width != 0){
                            $("#open").css("width", "0%");
                            isOpen = true;
                        }
                    }
                }
            }
        }
    }
    rawFile.send(null);
}

setInterval(readTextFile, 5);