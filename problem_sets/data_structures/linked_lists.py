class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"obj: {self.value}"


class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        value = Node(value)
        if not self.head:
            self.head = value
            self.tail = value
        else:
            # current = self.head
            # while current.next:
            #     current = current.next
            # current.next = value......works well!, but using tail will be more elegan
            self.tail.next = value
            self.tail = value
        
        self.length += 1

    def list_all(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    def pop(self):

        if not self.head:
            return None

        if self.length == 1:
            return self.head
            self.head = None
            self.tail = None    

        current = self.head
        while current.next:
            prev = current
            current = current.next

        prev.next = None
        self.tail = prev
        self.length -= 1

        return current

    def shift(self):
        if not self.head:
            return None
        current_head = self.head
        self.head = current_head.next
        self.length -= 1
        return current_head 

    def unshift(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def get_item(self, idx):
        if idx < 0 or idx >= self.length:
            return None

        current = self.head
        
        for a in range(idx):
            current = current.next
        return current

    def set_item(self, idx, value):
        item = self.get_item(idx)
        if item:
            item.value = value

    def insert(self, idx, value):
        if idx < 0 or idx > self.length:
            return False

        if idx == 0:
            self.unshift(value)
            return True

        new_node = Node(value)
        item = self.get_item(idx-1)
        new_node.next = item.next
        item.next =  new_node
        return True

    def remove_node(self, idx):
        if idx < 0 or idx > self.length-1:
            return False

        if idx == 0:
            return self.shift()
        elif idx == self.length-1:
            return self.pop()
        else:
            node = self.get_item(idx-1)
            node.next = node.next.next
            self.length -= 1
        return node 

    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_node= current.next
            current.next = prev
            prev = current
            current = next_node

        # self.head = prev
        # self.tail = self.get_item(self.length-1) worked 
        node = self.head
        self.head = self.tail
        self.tail = node




        





        

llst = Linked_list()


llst.push(10)
llst.push(11)
llst.push(12)
llst.push(13)

llst.list_all()
print("\n")
llst.reverse()
llst.list_all()
print("\n")
print(llst.tail)
# print(llst.get_item(2))
# print(llst.shift())
# print(llst.shift())
# print(llst.shift())
# print(llst.shift())
# print(llst.shift())
# print(llst.shift())
# llst.list_all()
# llst.unshift(100)
# llst.unshift(200)
# print("\n")
# llst.list_all()
# print(llst.get_item(2))

# print("\n")
# # llst.set_item(0,3333)
# print(llst.insert(0,777097))
# llst.list_all()
# print("\n")
# print(llst.get_item(2))


# print("\n")
# print("deleted",llst.remove_node(2))
# llst.list_all()
# print(llst.head)
# print("\n")
# print(llst.pop())
# llst.list_all()

# print("\n")
# print(llst.pop())
# llst.list_all()

# print("\n")
# print(llst.pop())
# llst.list_all()


# print("\n")
# print(llst.pop())
# llst.list_all()



# print("\n")
# print(llst.pop())
# llst.list_all()
