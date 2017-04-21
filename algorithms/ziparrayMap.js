    var arr1 = ["abc", 3, "yo"]
    var arr2 = [42, "wassup", true]
    var newObj = {};
    //can we assume we're getting two arrays of equal length?
    for(var idx in arr1){
        newObj[arr1[idx]] = arr2[idx]
    }
    console.log(newObj);
    return newObj;

function invertHash(obj){
    
}

