$(document).ready(function(){
    //create a thing that will create a card when button is clicked
    
    $('#addUser').click(function(){

        var f_name = $('#firstName').val();
        var l_name = $('#lastName').val();
        var desc = $('#description').val();
       
//check to make sure the entire form is filled out - if it isn't give an error
        if(f_name == "" || l_name == "" || desc == ""){
            alert("Please fill in the form");
        }
        //if the form is filled out send the first and last name to a pop up box then make that box click
        else {
            var cardData = "<div id='card'><p>" 
                + f_name 
                + " " 
                + l_name 
                + "<h4>Click to see description</h4></p>" 
                + "<p id='back'>" 
                + desc 
                + "</p></div>";
            alert(cardData);
            $("#rightPanel").append(cardData);

            $(document).on('click', '#card', function(){
                $(this).children().toggle();
            });



        }//end of else
    })//end of .on function for addUser


})// end of .ready function
