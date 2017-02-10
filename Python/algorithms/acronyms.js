var sentenceString = " there's no free lunch   -   gotta pay yer way. "

function stringAcronym(string){

    var newString = '';
    for(var idx = 0; idx < sentenceString.length-1; idx++){
        if(sentenceString[idx] == ' '){
            newString += sentenceString[idx+1];
        }
    } 
    console.log(newString.toUpperCase());
    return newString;
}

stringAcronym(sentenceString)



