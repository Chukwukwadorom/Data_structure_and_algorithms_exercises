import graphviz
from queue import Queue
      


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 0
    
    def __repr__(self):
        # return f"node: {self.__dict__}"
        return f"{self.value}"



class BTS:
    def __init__(self):
        self.root = None
    
    def __repr__(self):
        return f"BTS: {self.__dict__}"

    def insert(self, value):

        if not self.root:
            self.root = Node(value)
            return self

        cur_node  = self.root
        new_node = Node(value)

        while cur_node:

            if cur_node.value > new_node.value:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = new_node

            elif cur_node.value < new_node.value:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = new_node
            
            else:
                # maybe such node aalready exists, increase it
                cur_node.count += 1
                break

        return self

    def visualize_binary_tree(self):
        dot = graphviz.Digraph()
        dot.node(str(self.root.value))

        def add_nodes_edges(node):
            if node.left:
                dot.node(str(node.left.value))
                dot.edge(str(node.value), str(node.left.value))
                add_nodes_edges(node.left)
            if node.right:
                dot.node(str(node.right.value))
                dot.edge(str(node.value), str(node.right.value))
                add_nodes_edges(node.right)

        add_nodes_edges(self.root)
        dot.render('binary_tree', view=True, format='png')

    def search(self,value):
        if not self.root:
            return None

        current = self.root
        
        while current:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    return False
            elif value > current.value:
                if current.right:
                    current = current.right
                else:
                    return False
            else:
                return current

    def bfs(self):
        """breadth first search"""
        q =  []
        visited =  []
        current = self.root
        q.append(current)
        while True :
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            
            visited.append(q.pop(0))


            print(q)
            if len(q) !=0 :
                current = q[0]
            else:
                break
            

        return visited

    def dfs_pre_order(self):
        """depth first search """
        current = self.root
        visited = []
        
        def helper(current):
            visited.append(current.value)
            if current.left:
                helper(current.left)
            if current.right:
                helper(current.right)
        
        helper(current)

        return visited
    

    def dfs_post_order(self):
        """depth first search """
        current = self.root
        visited = []
        
        def helper(current):
            if current.left:
                helper(current.left)
            if current.right:
                helper(current.right)
            
            visited.append(current.value)
        
        helper(current)

        return visited

    def dfs_in_order(self):
        """depth first search """
        current = self.root
        visited = []
        
        def helper(current):
            if current.left:
                helper(current.left)

            visited.append(current.value)
            
            if current.right:
                helper(current.right)
            
           
        
        helper(current)

        return visited

    










bts = BTS()
# bts.insert(10)
# bts.insert(11)
# bts.insert(9)
# bts.insert(9)
# bts.insert(9)
# bts.insert(12)
# bts.insert(22)
# bts.insert(5)
# bts.insert(0)
# bts.insert(110)
# bts.insert(110)
keys = [30,5, 3, 7, 2, 4, 6, 8, 10,11,9,9,9,12,22,5,0,110,110, 10,5,13,11,2,16,7,10.5]
# keys= [10,5,13,11,2,16,7]
for key in keys:
    bts.insert(key)
print(bts)
bts.visualize_binary_tree()
vals = [111,444,7,98,2,0,1]

for val in vals:
    print(bts.search(val))

print("\n")
print(bts.bfs())


print("\n")
print(bts.dfs_pre_order())

print("\n")
print(bts.dfs_post_order())

print("\n")
print(bts.dfs_in_order())