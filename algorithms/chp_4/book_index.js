function getRanges(array) {
    var ranges = [];
    var begin = 0;
    var last = 0;
    for (var idx = 0; idx < array.length; idx++) {
        begin = array[idx];
        last = begin;
        while (array[idx + 1] - array[idx] == 1) { //while loop so go through until not true to get multiple sequential numbers
            last = array[idx + 1]; // increment the index if the numbers sequential
            idx++;
        }
        if(begin == last){
            if(begin == array[0]){//want no space to start, but a space befor each lone number and each number range
            ranges.push(begin)
            }
            else{
            ranges.push(" " + begin)
            }
        }
        else{
            ranges.push(" " + begin + "-" + last)
        }
    }
        stringRanges = '"' + ranges.join(',') + '"';
        console.log(stringRanges)
        return stringRanges;
}
var testArr=[1,13,14,15,37,38,70];
getRanges(testArr);
// want to return "1, 13-15, 37-38, 70"
