function printRange(start_point, end_point, counter){
 
    for(var i= start_point ; i< end_point-1; i+=counter){
        console.log(i);
    }
        
}

printRange(9,27,3);