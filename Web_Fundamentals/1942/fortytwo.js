//$(document).ready(function(){

var world = [
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,0,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,2],
    [2,1,2,2,1,2,2,2,1,1,1,1,2,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2],
    [2,1,2,1,1,2,3,2,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,2,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,2,2,1,1,2,2,2,1,1,1,1,2],
    [2,1,1,2,1,2,1,1,1,1,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,2,1,2,1,1,2,1,2,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2],
    [2,1,1,2,1,2,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,2,1,2,1,1,1,1,1,1,2,1,2,2,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,2,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2],
    [2,1,1,1,1,2,1,2,1,1,1,1,2,1,1,1,1,4,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,2,1,2,1,1,1,1,2,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,2,2,2,2,1,1,2],
    [2,1,1,2,1,2,1,1,1,1,2,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,2,1,2,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,2,2],
    [2,3,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
];

var score = 0;

var pacman = {
    x: 1,
    y: 1
};

function displayWorld(){
    var output = '';
    for(var i = 0; i < world.length; i++){
        output += "\n<div class = 'row'>\n";
        for(var j = 0; j < world[i].length; j++){
            if(world[i][j] == 2)
                output += "<div class = 'brick'></div>";
            
            else if (world[i][j] == 1)
                output += "<div class = 'coin'></div>";
            
            if (world[i][j] == 0)
                output += "<div class = 'empty'></div>"; 

            else if (world[i][j] == 3)
                output += "<div class = 'powerPill'></div>";
            
            if (world[i][j] == 4)
                output += "<div class = 'cherry'></div>";
        }
        output += "\n</div>";
    }
    document.getElementById('world').innerHTML = output;
}

function displayPacman(){ //updates the location of pacman
    document.getElementById('pacman').style.left = pacman.x * 20 + "px";
    document.getElementById('pacman').style.top = pacman.y * 20 +"px";
}

function displayScore(){ //updates the score when passing over a coin
    document.getElementById('score').innerHTML = score;
}

displayWorld();
displayPacman();
displayScore();

document.onkeydown = function(e){ //defines movement for pacman
    if(e.keyCode == 37 && world[pacman.y][pacman.x-1] != 2){
        $('#pacman').css("-webkit-transform", "rotate(180deg)");
        pacman.x--;
        
    }
    else if(e.keyCode == 39 && world[pacman.y][pacman.x+1] != 2){
       $('#pacman').css("-webkit-transform", "rotate(0deg)");
        pacman.x++;
        
    }
    else if(e.keyCode == 38 && world[pacman.y-1][pacman.x] != 2){
        $('#pacman').css("-webkit-transform", "rotate(-90deg)");
        pacman.y--;
    
    }
    else if(e.keyCode == 40 && world[pacman.y+1][pacman.x] != 2){
        $('#pacman').css("-webkit-transform", "rotate(90deg)");
        pacman.y++;
    }
    
  if(world[pacman.y][pacman.x] == 1){ //pacman eating the pill and getting points
      world[pacman.y][pacman.x] = 0;
      score += 5;
      displayWorld();
      displayScore();
 }

 if(world[pacman.y][pacman.x] == 3){ //pacman eating the powerpill and getting double points
      world[pacman.y][pacman.x] = 0;
      score *= 2;
      displayWorld();
      displayScore();
 }

 if(world[pacman.y][pacman.x] == 4){ //pacman eating the cherry and getting points
      world[pacman.y][pacman.x] = 0;
      score += 20;
      displayWorld();
      displayScore();
 }

 
 displayPacman();    

}