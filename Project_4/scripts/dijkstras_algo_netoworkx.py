''' Find the shortest path from Arad to Bucharest 
using Dijkstra's algorithm and networkx library.'''

import networkx as nx
from itertools import count
from heapq import heappush, heappop
import matplotlib.pyplot as plt

def plot_graph(graph):
    position = nx.spring_layout(graph)
    nx.draw(graph, position, with_labels=True)
    nx.draw_networkx_edge_labels(graph, position, font_size=8)
    plt.show()

def dijkstra_shortest_path(graph, source, target):
    ''' Return the shortest weighted path from source to target
    using Dijkstra's algorithm. '''
    assert source in graph, 'Such source node doesn\'t exist'
    assert target in graph, 'Such target node doesn\'t exist'

    push = heappush
    pop = heappop
    dist = {} # dictionary of final distances
    paths = {source: [source]}  # dictionary of paths
    seen = {source: 0} # dictionary of seen nodes

    # fringe is heapq with 3-tuples (distance,c,node)
    # use the count c to avoid comparing nodes (may not be able to)
    c = count()
    fringe = []

    push(fringe, (0,next(c), source))

    G_succ = G._adj
    get_weight = lambda u, v, data: data.get('weight', 1)

    while fringe:
        (d, _, v) = pop(fringe)
        if v in dist:
            continue  # already searched this node.
        dist[v] = d
        if v == target:
            break

        for u, e in G_succ[v].items():
            cost = get_weight(v, u, e)
            if cost is None:
                continue
            vu_dist = dist[v] + cost
            if u in dist:
                if vu_dist < dist[u]:
                    raise ValueError('Contradictory paths found:',
                                     'negative weights?')
            elif u not in seen or vu_dist < seen[u]:
                seen[u] = vu_dist
                push(fringe, (vu_dist, next(c), u))
                if paths is not None:
                        paths[u] = paths[v] + [u]

    if paths is not None:
        return (dist, paths)
    return dist

if __name__ == '__main__':
    # load graph as G from the file
    with open('Bucharest_graph.adjlist', 'rb') as f:
        G = nx.read_multiline_adjlist(f)

    # graph info and plot
    print(nx.info(G))
    #plot_graph(G)

    # build-in function check
    print(nx.algorithms.shortest_path(G, source='Arad', target='Bucharest', 
                                    weight='weights', method='dijkstra'))

    # custom function check
    print(dijkstra_shortest_path(G, source='Arad', target='Bucharest'))
