class Graph:
    def __init__(self):
        self.adjacent_list = {}

    def insert_vertex(self, vertex):
        if not self.adjacent_list.get(vertex):
            self.adjacent_list[vertex] = []

    def insert_edge(self, vertex1, vertex2, weight):
        self.adjacent_list[vertex1].append({"node":vertex2, "weight":weight})
        self.adjacent_list[vertex2].append({"node":vertex1, "weight":weight})

    def remove_edge(self, vertex1, vertex2):
        if self.adjacent_list.get(vertex1)  and self.adjacent_list.get(vertex2):
            for key, value self.adjacent_list.get(vertex1).remove(vertex2)
            self.adjacent_list.get(vertex2).remove(vertex1)

    def remove_vertex(self, vertex):
        pass

    

