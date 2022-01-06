class Vertex:
    def __init__(self, name):
        self.name = name
        self.connected_to = {}

    def name_get(self):
        return self.name

    def neighbor_add(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def neighbor_get(self):
        return self.connected_to.keys()

    def calcWeight(self, neighbor):
        if neighbor in self.connected_to:
            return self.connected_to[neighbor]
        else:
            return float("inf")


class Graph:
    def __init__(self):
        self.vertices_list = {}
        self.n_vertices = 0

    def edge_add(self, f_vertex, t_vertex, weight):
        if f_vertex not in self.vertices_list:
            self.vertice_add(f_vertex)
        if t_vertex not in self.vertices_list:
            self.vertice_add(t_vertex)
        self.vertices_list[f_vertex].neighbor_add(t_vertex, weight)

    def vertice_add(self, name):
        self.n_vertices += 1
        self.vertices_list[name] = Vertex(name)


    def vertice_get(self, name):
        if name in self.vertices_list:
            return self.vertices_list[name]
        else:
            return None

    def get_vertices(self):
        return self.vertices_list.keys()


class KruskalsAlgo:
    # Make a one-of-a-kind list of edges.
    def __init__(self, graph):
        self.edges = {}
        self.sets = {}
        T = []
        # make a list of edges that are sorted
        for x in graph.vertices_list.keys():
            connections = graph.vertices_list[x].connected_to
            for y in connections.keys():
                edge_name = x + '-' + y
                reverse = y + '-' + x
                if reverse not in self.edges.keys():
                    self.edges[edge_name] = connections[y]
        self.edges = sorted(self.edges.items(), key=lambda x: (x[1], x[0]))
        # make a set for each vertice
        for x in graph.vertices_list.keys():
            self.sets[x] = [x, 1]

    def MinimumSpanningTree(self, graph):
        T = []
        for x in self.edges:
            u = x[0][0]
            v = x[0][2]
            if self.find_parent(u) != self.find_parent(v):
                T.append(x)
                self.union(u, v)
        weight = 0
        edges_list = ''
        for x in T:
            weight += x[1]
            edges_list += x[0] + ', '
        edges_list = edges_list[:len(edges_list) - 2]
        print("Total Weight of Minimum Spanning Tree = " + str(weight))
        print("Node List = " + str(sorted(graph.vertices_list.keys())) + ", Edge List = {" + edges_list + '}')
        return T

    # Identify the disjoint set to which the vertex belongs.
    def find_parent(self, child):
        if (self.sets[child][0] == child):
            return child
        else:
            return self.find_parent(self.sets[child][0])

    def union(self, u, v):
        if (self.sets[self.find_parent(u)][1] > self.sets[self.find_parent(v)][1]):
            self.sets[v][0] = self.sets[u][0]
        elif (self.sets[self.find_parent(u)][1] > self.sets[self.find_parent(v)][1]):
            self.sets[u][0] = self.sets[v][0]
        else:
            self.sets[self.find_parent(u)][0] = self.sets[v][0]
            self.sets[self.find_parent(v)][1] += 1


def main():
    g = Graph()
    g.edge_add('A', 'B', 10)
    g.edge_add('A', 'C', 48)
    g.edge_add('A', 'D', 11)

    g.edge_add('B', 'A', 71)
    g.edge_add('B', 'C', 1)
    g.edge_add('B', 'F', 66)
    g.edge_add('B', 'H', 34)

    g.edge_add('C', 'A', 32)
    g.edge_add('C', 'B', 72)
    g.edge_add('C', 'D', 31)
    g.edge_add('C', 'E', 82)
    g.edge_add('C', 'F', 68)

    g.edge_add('D', 'A', 81)
    g.edge_add('D', 'C', 31)
    g.edge_add('D', 'E', 79)
    g.edge_add('D', 'I', 50)

    g.edge_add('E', 'C', 65)
    g.edge_add('E', 'D', 33)
    g.edge_add('E', 'F', 18)
    g.edge_add('E', 'G', 23)

    g.edge_add('F', 'B', 36)
    g.edge_add('F', 'C', 42)
    g.edge_add('F', 'E', 18)
    g.edge_add('F', 'G', 39)
    g.edge_add('F', 'H', 24)

    g.edge_add('G', 'E', 26)
    g.edge_add('G', 'F', 42)
    g.edge_add('G', 'H', 28)
    g.edge_add('G', 'I', 24)

    g.edge_add('H', 'B', 36)
    g.edge_add('H', 'F', 22)
    g.edge_add('H', 'G', 25)
    g.edge_add('H', 'I', 18)

    g.edge_add('I', 'D', 34)
    g.edge_add('I', 'G', 23)
    g.edge_add('I', 'H', 17)

    k = KruskalsAlgo(g)
    k.MinimumSpanningTree(g)


if __name__ == "__main__":
    main()