class Graph:
    def __init__(self):
        self.adjacent_list = {}

    def add_vertex(self, key):
        if not self.adjacent_list.get(key):
            self.adjacent_list[key] = []
    
    def add_edge(self, vertex1, vertex2):
        # if  not self.adjacent_list.get(vertex1) and not self.adjacent_list.get(vertex2):
        self.adjacent_list[vertex1].append(vertex2)
        self.adjacent_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if  self.adjacent_list.get(vertex1) and self.adjacent_list.get(vertex2):
            self.adjacent_list[vertex1].remove(vertex2)
            self.adjacent_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):

        if not self.adjacent_list.get(vertex):
            return
        
        edges = self.adjacent_list.get(vertex)

        for edge in edges:
            self.remove_edge(vertex, edge)
        
        del self.adjacent_list[vertex]

    def dft_recursive (self):
        """depth first traversal recursion"""
        result = []
        visited = {}

        vertex = list(self.adjacent_list.keys())[0]

        def helper(vertex):
            if not visited.get(vertex):
                result.append(vertex)
                visited[vertex] = True
                for new_vertex in self.adjacent_list[vertex]:           
                    helper(new_vertex)

        helper(vertex)
        return result

    def dft_iteration(self):
         """depth first traversal iteration"""
         stack = []
         result = []
         visited = {}

         vertex = list(self.adjacent_list.keys())[0]
         stack.append(vertex)
         while len(stack):
            vertex = stack.pop(-1)
            # vertex = stack.pop(0)....would be breadth first
            if not visited.get(vertex):
                visited[vertex] = True
                result.append(vertex)

                for vert in self.adjacent_list[vertex]:
                    stack.append(vert)
        
         return result

    def bft_iteration(self):
        """breadth first search iteration"""
        queue = []
        visited = {}
        result = []
        vetex = list(self.adjacent_list.keys())[0]
        queue.append(vetex)

        while len(queue):
            vertex = queue.pop(0)
            if not visited.get(vertex):
                result.append(vertex)
                visited[vertex] =  True

                for vert in self.adjacent_list[vertex]:
                    queue.append(vert)

        return result


            




       










    

graph = Graph()
# graph.add_vertex("Dallas")
# graph.add_vertex("Tokyo")
# graph.add_vertex("Zurich")
# graph.add_vertex("Oslo")

# graph.add_edge("Dallas", "Oslo")
# graph.add_edge("Tokyo", "Zurich")


# print(graph.adjacent_list)
# # graph.remove_edge("Dallas", "Oslo")
# # graph.remove_edge("Tokyo", "Zurich")

# graph.remove_vertex("Oslo")
# print(graph.adjacent_list)

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")

graph.add_edge("A","B")
graph.add_edge("A","C")
graph.add_edge("B","D")
graph.add_edge("C","E")
graph.add_edge("D","E")
graph.add_edge("D","F")
graph.add_edge("E","F")

print(graph.adjacent_list)

print("recursion", graph.dft_recursive())
print("iteration", graph.dft_iteration())
print("breadth first iteration", graph.bft_iteration())