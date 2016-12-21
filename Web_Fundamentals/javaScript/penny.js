var sum = 0;
var payment = 0.01;

for (var i = 1; i < 30; i++){
    sum += payment;
    payment += payment;
}
