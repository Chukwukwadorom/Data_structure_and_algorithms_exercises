"""SLL - pop exercise
Implement the following on the SinglyLinkedList.prototype:

pop

This function should remove a node at the end of the SinglyLinkedList.
 It should return the node removed.

Examples

var singlyLinkedList = new SinglyLinkedList();
 
singlyLinkedList.push(5); // singlyLinkedList
singlyLinkedList.length; // 1
singlyLinkedList.head.val; // 5
singlyLinkedList.tail.val; // 5
 
singlyLinkedList.push(10); // singlyLinkedList
singlyLinkedList.length; // 2
singlyLinkedList.head.val; // 5
singlyLinkedList.head.next.val; // 10
singlyLinkedList.tail.val; // 10
 
singlyLinkedList.push(15); // singlyLinkedList
singlyLinkedList.length; // 3
singlyLinkedList.head.val; // 5
singlyLinkedList.head.next.val; // 10
singlyLinkedList.head.next.next.val; // 15
singlyLinkedList.tail.val; // 15
 
singlyLinkedList.pop().val; // 15
singlyLinkedList.tail.val; // 10
singlyLinkedList.length; // 2
singlyLinkedList.pop().val; // 10
singlyLinkedList.length; // 1
singlyLinkedList.pop().val; // 5
singlyLinkedList.length; // 0
singlyLinkedList.pop(); // undefined
singlyLinkedList.length; // 0"""

class Node:
    def __init__(self, value):
        self.next = None
        self.val  = value

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        
        self.tail.next = new_node
        self.tail = new_node

        self.length += 1
        return self


    def pop(self):
        popped = self.tail
        if self.length == 0:
            return popped
        elif self.length == 1:
            self.tail = None
            self.head = None
        
        else:
            current = self.head
            while current:
                if current.next == self.tail:
                    self.tail = current
                    self.tail.next = None
                    break
                current = current.next
        
        self.length -= 1
        return popped 

    def get (self, idx):
        
        if not self.head:
            return None

        current = self.head
        counter = 0

        while current:
            if counter == idx:
                return current
            current = current.next
            counter += 1
        
        return None

    def insert (self,idx, value):
        if idx == 0:
            self.unshift(value)
        elif idx == self.length:
            self.push(value)
        elif idx > self.length:
            return False   
        else:
            new_node = Node(value)
            prev = self.get(idx - 1 )
            new_node.next = prev.next
            prev.next = new_node
            
        self.length += 1 
        return True

    def unshift(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def rotate(self, idx):
        if not self.head or idx < 0 or idx > self.length:
            return None
        
        if idx == 0:
            start_node = self.head
            stop_node =  self.tail
        else:
            self.tail.next = self.head
            stop_node = self.get(idx-1)
            start_node =  self.get(idx)

        
        current = start_node
        while current != stop_node:
            values.append(current.val)
        
        self.tail.next = None
        return values

       





singlyLinkedList = SLL()

singlyLinkedList.push(5).push(10).push(15).push(20).push(25);
singlyLinkedList.head.val; // 5
singlyLinkedList.tail.val; // 25;
 
singlyLinkedList.rotate(3);
singlyLinkedList.head.val; // 20
singlyLinkedList.head.next.val; // 25
singlyLinkedList.head.next.next.val; // 5
singlyLinkedList.head.next.next.next.val; // 10
singlyLinkedList.head.next.next.next.next.val; // 15
singlyLinkedList.tail.val; // 15
singlyLinkedList.tail.next; // null
var singlyLinkedList = new SinglyLinkedList;
singlyLinkedList.push(5).push(10).push(15).push(20).push(25);
singlyLinkedList.head.val; // 5
singlyLinkedList.tail.val; // 25;
 
singlyLinkedList.rotate(-1);
singlyLinkedList.head.val; // 25
singlyLinkedList.head.next.val; // 5
singlyLinkedList.head.next.next.val; // 10
singlyLinkedList.head.next.next.next.val; // 15
singlyLinkedList.head.next.next.next.next.val; // 20
singlyLinkedList.tail.val; // 20
singlyLinkedList.tail.next // null
var singlyLinkedList = new SinglyLinkedList;
singlyLinkedList.push(5).push(10).push(15).push(20).push(25);
singlyLinkedList.head.val; // 5
singlyLinkedList.tail.val; // 25;
 
singlyLinkedList.rotate(1000)
print(singlyLinkedList.head.val)
print(singlyLinkedList.head.next.val)
print(singlyLinkedList.head.next.next.val)
print(singlyLinkedList.head.next.next.next.val)
print(singlyLinkedList.head.next.next.next.next.val)
print(singlyLinkedList.tail.val)
print(singlyLinkedList.tail.next)

# singlyLinkedList.push(5).push(10).push(15).push(20)
# print(singlyLinkedList.insert(2,12))
# print(singlyLinkedList.insert(100,12))
# print(singlyLinkedList.length)
# print(singlyLinkedList.head.val) 
# print(singlyLinkedList.head.next.val) 
# print(singlyLinkedList.head.next.next.val) 
# print(singlyLinkedList.head.next.next.next.val)
# print(singlyLinkedList.head.next.next.next.next.val) 
 
# print(singlyLinkedList.insert(5,25))
# print(singlyLinkedList.head.next.next.next.next.next.val) 
# print(singlyLinkedList.tail.val) 

# singlyLinkedList.push(5).push(10).push(15).push(20)
# print(singlyLinkedList.get(0).val)
# print(singlyLinkedList.get(1).val)
# print(singlyLinkedList.get(2).val)
# print(singlyLinkedList.get(3).val)
# print(singlyLinkedList.get(4)) 
 
# singlyLinkedList.push(5)
# print(singlyLinkedList.length)
# print(singlyLinkedList.head.val)
# print(singlyLinkedList.tail.val)
 
# print("\n") 
# singlyLinkedList.push(10)
# print(singlyLinkedList.length)
# print(singlyLinkedList.head.val)
# print(singlyLinkedList.head.next.val)
# print(singlyLinkedList.tail.val)
 
# print("\n")
# singlyLinkedList.push(15)
# print(singlyLinkedList.length)
# print(singlyLinkedList.head.val)
# print(singlyLinkedList.head.next.val)
# print(singlyLinkedList.head.next.next.val)
# print(singlyLinkedList.tail.val)
 
# print("\n")
# print(singlyLinkedList.pop().val)
# print(singlyLinkedList.tail.val)
# print(singlyLinkedList.length)
# print(singlyLinkedList.pop().val)
# print(singlyLinkedList.length)
# print(singlyLinkedList.pop().val)
# print(singlyLinkedList.length)
# print(singlyLinkedList.pop())
# print(singlyLinkedList.length)