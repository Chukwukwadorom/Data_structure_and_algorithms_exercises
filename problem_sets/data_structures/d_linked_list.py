class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"obj:{self.value}"
        # return f"{self.__dict__}"


class Double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        
        self.tail = new_node
        self.tail.next = None
        self.length += 1
        return True

    def list_all(self):
        current = self.head
        while current:
            print(current)
            current=current.next

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

    def unshift(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head= new_node
            self.tail= new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def get(self, idx):

        mid_way = self.length//2
        counter = None

        if idx < 0 or idx >= self.length:
            return None
        elif idx < mid_way:
            current = self.head
            counter = 0
            while counter != idx:
                current = current.next
                counter += 1
        else:
            current = self.tail
            counter = self.length-1
            while counter != idx:
                current = current.prev
                counter -= 1
        return current

    def set_item(self,idx, value):
        node = self.get(idx)
        if node:
            node.value = value
            return True  
        else:
            return False 

    def insert(self, idx, value):

        if idx < 0 or idx > self.length -1:
            return False
        elif idx == 0:
            self.unshift(value)
        elif idx == self.length-1:
            self.push(value)
        else:
            new_node = Node(value)

            prev_node = self.get(idx-1)
            new_node.prev = prev_node
            new_node.next = prev_node.next
            prev_node.next = new_node
            new_node.next.prev = new_node

        self.length += 1
        return True 

    def remove(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        elif idx == 0:
            return self.shift()
        elif idx == self.length-1:
            return self.pop()

        else:
            node = self.get(idx)
            node.next.prev = node.prev
            node.prev.next = node.next
            node.prev = None
            node.next = None

            return node
        self.length -= 1


            



        
        




dll = Double_linked_list()

dll.push(10)
dll.push(11)
dll.push(100)

# dll.list_all()
print("\n")
dll.unshift(200)
dll.unshift(500)
dll.unshift(300)
dll.unshift(400)

dll.list_all()

print("\n")
print("index:",dll.get(5))

# print("get:",dll.set_item(5,7777777))
dll.list_all()
print("\n")

dll.insert(3,40)
dll.list_all()
print("\n")
print("removed:",dll.remove(4))
dll.list_all()
# print("popped:",dll.pop())
# print("popped:",dll.pop())
# print("popped:",dll.pop()) 
# print("popped:",dll.pop())
# print("popped:",dll.pop())    
# dll.list_all()


# print("\n")
# print("shift:",dll.shift())
# print("shift:",dll.shift())
# print("shift:",dll.shift()) 
# print("shift:",dll.shift())
# print("shift:",dll.shift())    
# dll.list_all()