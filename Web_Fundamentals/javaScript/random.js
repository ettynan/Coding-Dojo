var win = 100;
var coins = Math.floor(Math.random()*50)+1;

function lottery(change){
    while(change > 0){
        var chance = Math.floor(Math.random()*100)+1;
        if(chance !=win){
            change--;
        }
        
        else{
            var winnings = Math.floor(Math.random()*51)+50;
            change=coins + change;
        }
    }
    
    console.log("You have "+ coins);
    console.log("You won "+ winnings);
    console.log("Money "+ change);
}

lottery(coins);