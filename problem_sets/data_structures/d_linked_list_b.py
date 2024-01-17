class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return f"obj:{self.value}"


class Doubly_linked_list:

    def __init__(self):
        self.head =  None
        self.tail = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
       popped = None
        if self.length <= 0:
            return popped
        elif self.length == 1:
            popped = self.head
            self.head = None
            self.tail = None
        else:
            popped = self.tail
            self.tail = popped.prev
            popped.prev = None
            self.tail.next = None

        self.length -= 1    

        return popped

    def list_all(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def unshift(self, value):
        new_node = Node(value)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

        self.length += 1

        return self

    def shift(self):
        
        old_head = self.head
        if self.length == 0:
            return old_head
        elif self.length == 1:
            self.head = None
            self.tail = None
            return old_head
        
        self.head = old_head.next
        old_head.next = None
        self.head.prev = None

        self.length -= 1
        return old_head

    def get(self,idx):
        if idx < 0 or idx >=self.length:
            return None
        
        mid_point = self.length//2
        current = self.head
        if idx < mid_point:
            counter = 0
            while idx != counter:
                current = current.next
                counter +=1 
        else:
            counter = self.length-1
            current = self.tail
            while idx != counter:
                current = current.prev
                counter -= 1 

        return current

    def set_item(self,idx,value):
        node = self.get(idx)
        if node:
            node.value = value
            return True
        else:
            return False

    def remove(self,idx):
        if idx < 0 or idx >= self.length:
            return None
        elif idx == 0:
            return self.self()
        elif idx == self.length-1:
            return self.pop()



        

    

dll = Doubly_linked_list()
dll.push(5)
print(dll.length)
print(dll.head.value)
print(dll.tail.value)
print(dll.head.prev) 
dll.push(10) 
print(dll.length)
dll.unshift(12)
dll.unshift(11)
print("\n")
dll.list_all()

dll.shift()
print("\n")
dll.list_all()
print("\n")
print(dll.get(2))
print("popped:",dll.pop())
print("popped:",dll.pop())
print("popped:",dll.pop())
print("popped:",dll.pop())
dll.list_all()