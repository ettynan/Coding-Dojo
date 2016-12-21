$(document).ready(function(){

    $('img').hover(function(){
        var temp = $(this).attr('src');
        var altnew = $(this).attr('data-alt-src');
        $(this).attr('src', altnew);
        $(this).attr('data-alt-src', temp);
    });

});
