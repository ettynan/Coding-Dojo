$(document).ready(function(){
    $(document).on()
    
    for (var i = 1; i < 152; i++){
    var imagePath = " src=http://pokeapi.co/media/img/";
    var pokePic = "<img id=" + i + imagePath + i + ".png>";
    $("#mainImages").append(pokePic); // use pokePic not imagePath to get the actual images not the urls
    
    }//end of for loop for image and info loading

     $("img").click(function(){
        var id = (this).id;
        var grab = "http://pokeapi.co/api/v1/pokemon/" + id + "/";

        $.get(grab, function(result){ // types is the only one of the info that has multiple options so a for loop is needed ( they do not have multiple weights or heights)
            for(var l = 0; l < result.types.length; l++){//loop to get all the information, and loop through the types which may have more than one.
            
                var pokeInformation = "<h2>" + result.name + "</h2>"
                                        +  "<img" + imagePath + id  + ".png>" 
                                        + "<h3>Types</h3>" + "<li>" + result.types[l].name + "</li>"
            }
                pokeInformation = pokeInformation  + "<h3>Weight</h3>" + "<li>" + result.weight + "</li>";

                $("#pokeInfo").html(pokeInformation);
        }, "json")


   }); //end of img function

});//end of .ready function //trello
