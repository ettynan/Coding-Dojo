$(document).ready(function(){

    $('img').click(function(){
        var temp = $(this).attr('src');
        var altnew = $(this).attr('data-alt-src');
        $(this).attr('src', altnew);
        $(this).attr('data-alt-src', temp);
    });

});
