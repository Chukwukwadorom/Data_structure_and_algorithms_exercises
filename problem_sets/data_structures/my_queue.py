class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.value}"

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    
    def enq (self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
    
    def denq(self):
        if not self.head:
            return None
        else:
            old_head = self.head
            new_head = self.head.next
            old_head.next = None
            self.head = new_head

            self.length -= 1

            return old_head.value
    
    def list_all(self):
        current = self.head

        while current:
            print(current)
            current = current.next
        

if __name__ == "__main__":

    ls = [1,2,3,4,5,6]

    queue  = Queue()
    for elem in ls:
        queue.enq(elem)

    queue.list_all()
    print("\n")
    for _ in range(len(ls)+3):
        print("unshifting",type(queue.denq()))


        
            
