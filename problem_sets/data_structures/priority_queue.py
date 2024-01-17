class Node:
    def __init__(self,item, priority):
        self.item = item
        self.priority = priority

    def __repr__(self):
        return f"{self.priority}"


class Priority_queue:
    def __init__ (self):
        self.values = []

    def enqueue (self, item, priority):
        new_node = Node(item, priority)
        self.values.append(new_node)

        def bubble_up():
            cidx = len(self.values) - 1 
            while cidx > 0:
                pidx = (cidx-1) // 2

                if self.values[pidx].priority > self.values[cidx].priority:
                    self.values[pidx],self.values[cidx] = self.values[cidx],self.values[pidx]
                    cidx = pidx

                else:
                    break
           
        bubble_up()

    def denqueue(self):
        full_length = len(self.values)
        if full_length  == 0:
            return None

        self.values[0],self.values[-1] = self.values[-1],self.values[0]

        popped = self.values.pop(-1)

        full_length -= 1

        def sink_down():
           
            pidx = 0

            while pidx < full_length:
                left_child_idx = (pidx*2 + 1)
                right_child_idx = (pidx*2 + 2)

                if left_child_idx >= full_length  and right_child_idx >= full_length:
                    break
                elif right_child_idx >= full_length:
                    new_idx = left_child_idx
                else:
                    new_idx = left_child_idx if self.values[left_child_idx].priority < self.values[right_child_idx].priority else right_child_idx


                if self.values[pidx].priority > self.values[new_idx].priority:
                    self.values[pidx] , self.values[new_idx] = self.values[new_idx] , self.values[pidx]

                    pidx = new_idx
                else:
                    break

        if full_length >= 2:
            sink_down()
            return popped

                


 


        


                    
pq = Priority_queue()
vals = [41,39,33,18,27,12,55]
items = ["code", "food", "write", "medicine", "travel", "love", "day dream"]

for val in range(len(vals)):
   priority = vals[val]
   item = items[val]
   pq.enqueue(item, priority)



print(pq.values)

# pq.denqueue()
print("\n")

for val in range(len(vals)):
    pq.denqueue()
    print("after denqueue",pq.values)
   



                



                

