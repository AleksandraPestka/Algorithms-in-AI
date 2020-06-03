''' 
Implement graph by hand. Find the shortest path 
from Arad to Bucharest using Dijkstra's algorithm.
Based on : https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
'''

from collections import deque, namedtuple

Edge = namedtuple('Edge', 'start, end, weight')

class Graph:
    def __init__(self, file_path):
        edges = self.load_edges(file_path)
        self.check_correctness(edges)
        self.edges = [self.make_edge(*edge) for edge in edges]
        
    def load_edges(self, file_path):
        ''' Load edges from .txt file'''

        edges = []
        with open(file_path, 'r') as tmp_file:
            for line in tmp_file:
                lst_data = line[:-1].split(' ')
                tuple_data = (lst_data[0], lst_data[1], int(lst_data[2]))
                edges.append(tuple_data)

        return edges

    def check_correctness(self, edges):
        ''' Check if edge has 3 elements (start, end, weight) '''

        wrong_edges = [i for i in edges if len(i) != 3]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

    def make_edge(self, start, end, weight=1):
        ''' Make weighted edge (unweighted by default). '''

        return Edge(start, end, weight)

    @property
    def vertices(self):
        ''' Find all unique vertices. '''

        ver = set(sum(([edge.start, edge.end] for edge in self.edges), []))
        return ver

    def get_node_pairs(self, node1, node2, both_ends=True):
        ''' Return nodes pair. '''

        if both_ends:
            node_pairs = [[node1, node2], [node2, node1]]
        else:
            node_pairs = [[node1, node2]]
        return node_pairs

    def remove_edge(self, node1, node2, both_ends=True):
        '''Remove connection between two nodes. '''

        node_pairs = self.get_node_pairs(node1, node2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, node1, node2, weight=1, both_ends=True):
        node_pairs = self.get_node_pairs(node1, node2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(node1, node2))

        self.edges.append(Edge(start=node1, end=node2, weight=weight))
        if both_ends:
            self.edges.append(Edge(start=node2, end=node1, weight=weight))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}

        # take into consideration two directions
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.weight))
            neighbours[edge.end].add((edge.start, edge.weight))

        return neighbours

    def find_shortest_path(self, source, target):
        ''' Find the shortest path between source and target node
        using Dijkstra's algorithm. '''

        assert source in self.vertices, 'Provided source does not exist.'
        assert target in self.vertices, 'Provided target does not exist.'

        # create dictionaries with distances and visited nodes
        # set the distance to inf for nodes except the initial one 
        distances = {vertex: float('inf') for vertex in self.vertices}
        previous_vertices = {vertex: None for vertex in self.vertices}

        # set the distance to zero for initial node
        distances[source] = 0
        vertices_unvisited = self.vertices.copy()

        # untill the vertices list is empty 
        while vertices_unvisited:
            # select the unvisited node with the smallest distance 
            current_vertex = min(vertices_unvisited, 
                                 key=lambda vertex: distances[vertex])
            # remove current node from unvisited nodes list
            vertices_unvisited.remove(current_vertex)

            if distances[current_vertex] == float('inf'):
                break

            # find unvisited neighbours for the current node
            for neighbour, weight in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + weight

                # save the smaller distance 
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), target
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)

        return path

if __name__ == '__main__':
    graph_path = r'../graph_data/Arad_Bucharest_edges.txt'
    graph = Graph(graph_path)

    source = 'Arad'
    target = 'Bucharest'
    print(f'The shortest path from {source} to {target}')
    print(graph.find_shortest_path(source, target))

