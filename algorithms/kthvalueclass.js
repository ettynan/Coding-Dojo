function Node(data) {
    this.data = data;
    this.next = null;
}
function LinkedList() {
    this.head = null;
}

var list = Sll();

Sll.prototype.kthlast = function(k){
    if ((k<1)|| (!this.head)){
        return null;
    }
    var current = this.head;
    var counter = 0;
    while(current.next){  //go until end which has value of null 
        counter++;
        current = current.next;
    }
    if (counter - k < 1) throw new Error('nope');
    current = this.head;
    var iterate = current - k;
    while(iterate){
        console.log(iterate);
        iterate--;
        console.log(current.data + "data");
        current = current.next;
    }
    return current;
}

console.log(list.kthlast(1));

BETTER
Sll.prototype.kthlast2(1){
    if ((k<1)|| (!this.head)){
        return null;
    }
    var current = this.head;
    while(current && k){  //go until end which has value of null 
        current = current.next;
        k--;
    }
    if(k) throw new Error('no range');
    var follower = this.head;
    while (current){
        current = current.next;
        follower = follower.next;
    }
    return follower.data;
}