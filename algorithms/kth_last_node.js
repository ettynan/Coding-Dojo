
function Node(data) {
    this.data = data;
    this.next = null;
}
function LinkedList() {
    this.head = null;
}

LinkedList.prototype.push=function(val){
    var node = {
        value: val,
        next: null
    }
    if(!this.head){
        this.head = node;
    }
    else{
        current = this.head;
        while(current.next){
            current = current.next;
        }
        current.next = node;
    }
}

function nodeFromEnd(sll, nodePosition){
    var node = sll.head;
    var index = 1;
    var kthNode;
    // if nodePosition is 0 or negative
    if(nodePosition<=0){
        console.log('This is not a valid node from end position');
        return;
    }
    while(node){
        if(index == nodePosition){
            kthNode = sll.head;
        }
        else if((index-nodePosition)>0){
            kthNode = kthNode.next;
        }
        index++;
        node = node.next;
    }
    return kthNode;
}

var sll = new LinkedList();
sll.push(1);
sll.push(2);
sll.push(3);
sll.push(4);
sll.push(5);

console.log(nodeFromEnd(sll, 5));


