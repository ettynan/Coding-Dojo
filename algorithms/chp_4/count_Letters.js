var sentenceString = "Honey pie, you are driving me crazy"
function stringLetterCount(string){

    var count = 0;
    for(var idx = 0; idx < sentenceString.length; idx++){
        if(sentenceString[idx] !== ' '){
            count++;
        }
    } 
    console.log(count);
    return count;    
}

stringLetterCount(sentenceString)