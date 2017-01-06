$(document).ready(function(){
    //function to create a card when a button is clicked
    $(".addUser").click(function(){
        // delclare variable to carry the typed in values
        var first = <td>$("#firstName").val()</td>;
        var last = <td>$("#lastName").val()</td>;
        var address = <td>$("#email").val()</td>;
        var number = <td>$("#phoneNum").val()</td>;

        // if statement to alert if all fiels are not filled in
        // if(first== "" || last== "" || address== "" || number== ""){
        //     alert("Please fill out the info!");
        // }
        // else{
            // function to put text in the <table>
            //create a new variable to hold the html to be inserted into the page
            var tableData = $(<tr>first + last + address + number</tr>    
            ).on("click", function(
                $("tbody").append(tableData);
    

    });

});
