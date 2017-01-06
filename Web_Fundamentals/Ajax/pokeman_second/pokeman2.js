$(document).ready(function(){

    for (var i = 1; i < 10; i++){
    var image = $(`<img class ="pokemanImage" data-pokemanId= "${i}" src= "http://54.70.82.18/media/${i}.png">`);
        $("#mainContent").append(image)
    }
     $("pokemanImage").on("click", function(){
         console.log(this);
     
     var pokeNum=$(this).data("pokemanID");    
         console.log= ("before.get" , pokeNum)
     
     
     $.get(`http://pokeapi.co/api/v1/pokemon/${i}`, function(result){
         console.log("Complete", reponse)
        // $.get(`http://pokeapi.co/api/v1/pokemon/${i}`, function(result){
            //  console.log("Complete", reponse)
 });


});


//     var name = 
//         console.log(res);
//         }, "json");
// });
// };

// }; $("#mainContent").append(image);





