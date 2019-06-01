preText = 1;

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
                
                        window.location.assign("fbNew.html#fbImg");
                
                    }
                }
            }
        }
    }
    rawFile.send(null);
}

setInterval(readTextFile, 5);