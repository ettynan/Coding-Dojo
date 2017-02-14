
// function remainShort(arr, len){
//     var newArray = {}
    
//     for(var idx = 0; idx < arr.length; idx++){
//         if(arr[idx] >= len){
//             newArray.push(arr[idx]);
//         }
//     } 
//     console.log(newArray);
//     return newArray;    
// }

// remainShort()

//in place
var arr = ["They", "You are"];
function remainShort(arr, len){
    for(var idx = 0; idx < arr.length; idx++){
        if(arr[idx] < len){
            arr.splice(idx, 1)
            idx--;
        }
    }
    console.log(arr);
    return arr;
}

remainShort(arr, 5)