function number_check(array){
  //parameter check
     var newArray = [];
    for (var i = 0; i< array.length; i++){
       //check for numbers and add only those
        if (typeof(array[i]) === "number"){
            newArray.push(array[i]);

        }

    }
//  console.log(newArray); printed twice
  return newArray;
}
// testing function
var testArray = [1, 5, "tynan"];
number_check(testArray);
