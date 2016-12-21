$(document).ready(function(){
    $("#click_button").click(function(){
        $("#chainmail").hide();
    });

    $("#click_button2").click(function(){
          $("#chainmail").show();
    });

    $("#click_button3").click(function(){
        $("#chainmail").toggle();
    });

    $("#click_button4").click(function(){
        $("#puppy").slideUp( "slow", function() {
    });
        });

    $( "#click_button5").click(function(){
        $("#puppy").slideDown( "slow", function() {
        });
    });

    $( "#click_button6").click(function() {
        $("#puppy" ).slideToggle( "slow", function() {
        });
    });

    $( "#click_button7").click(function() {
        $("#elephant").fadeIn( "slow", function() {
        });
    });

    $( "#click_button8").click(function() {
        $("#elephant").fadeOut( "slow", function() {
        });
    });

    $("#click_button9").click(function() {
        $(this).siblings("p").addClass("green")
        });

    $("#click_button10").click(function() {
        $(this).siblings("p").before("<h2>Hi Human!</h2>")
        });

    $("#click_button11").click(function() {
        $(this).siblings("p").after("<h2>Hi Human!</h2>")
        });

    $("#click_button12").click(function() {
        $(this).siblings("p").append("<h2>Hi Human!</h2>")
        });

    $("#click_button13").click(function() {
        $(this).siblings("p").html("<h2>Hi Human!</h2>")
        });

    $("#click_button14").click(function() {
        $("#kitten").attr("width","100")
        });

    $("#click_button15").click(function() {
        $(this).siblings("input").val("Pointy ears")
        });

    $("#click_button16").click(function() {
        $(this).siblings("p").text("Buh Bye!")
        });

    $("#click_button17").click(function() {
        $(this).parent().data("favorite color", "purple")
        });

    $("#click_button18").click(function() {
        $(this).siblings("p").html($(this).parent().data("favorite color"))
        });

});
