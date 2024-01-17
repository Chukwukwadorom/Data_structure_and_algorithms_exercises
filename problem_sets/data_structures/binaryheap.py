class Binary_heap:
    def __init__(self):
        self.values = []

    def insert(self, value):
        self.values.append(value)
        if len(self.values) >= 2:
            self.bubble_up()
        
        return self.values

    def bubble_up(self):
        """the parent node has to be bigger than the children"""
        cidx = len(self.values)-1
        pidx = (cidx - 1) // 2

        while pidx >= 0:
            if self.values[pidx] < self.values[cidx]:
                self.values[pidx], self.values[cidx] = self.values[cidx], self.values[pidx]
                cidx = pidx
                pidx = (cidx - 1) // 2
            else:
                break

    def extract_max(self):
        if len(self.values) == 0:
            return None
        
        self.values[0], self.values[-1] = self.values[-1], self.values[0] 
        popped = self.values.pop(-1)

        def sink_down():
            idx = 0

            while True:
                swapped = False
                left_idx = idx*2 +1
                right_idx = idx*2 +2
                if left_idx >=len(self.values) and right_idx >= len(self.values):
                    break
                elif right_idx >= len(self.values):
                    new_idx = left_idx
                else:
                    new_idx = left_idx if self.values[left_idx] > self.values[right_idx] else right_idx

                if self.values[new_idx] > self.values[idx]:
                    self.values[idx], self.values[new_idx] = self.values[new_idx], self.values[idx]
                    swapped = True
                    idx = new_idx
                
                if not swapped:
                    print("not swapped")
                    break

        if len(self.values) >= 2:
            sink_down()
            print(self.values)
        return popped



                




vals = [41,39,33,18,27,12,55]
# vals = [27,18,12]
bheap = Binary_heap()
for val in vals:
    print(bheap.insert(val))

print("\n")
# print(bheap.extract_max())

for _ in vals:
    bheap.extract_max()

            



        

