#!/usr/bin/python3
r"""
A solution using breadth-first search,
using a regular list as a queue.
"""

def main():
    # Read vertices from stdin
    num_vertices = int(input())
    vertices = list(range(num_vertices))

    # Read edges from stdin
    num_edges = int(input())
    edges = [int_pair(input()) for _ in range(num_edges)]

    # Construct the graph
    graph = Graph(vertices, edges)

    # Read queries from stdin
    num_queries = int(input())
    queries = [int_pair(input()) for _ in range(num_queries)]

    # Answer the queries on stdout
    for vertex1, vertex2 in queries:
        print('yes' if graph.has_path_between(vertex1, vertex2) else 'no')

def int_pair(string):
    pair = tuple(map(int, string.split()))
    if len(pair) != 2: raise ValueError('wrong number of items')
    return pair

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        neighbours = {v: set() for v in vertices}
        for v1, v2 in edges:
            neighbours[v1].add(v2)
            neighbours[v2].add(v1)
        self.neighbours = neighbours

    def has_path_between(self, vertex1, vertex2):
        visited = set()
        queue = [vertex1]
        while queue:
            v = queue.pop(0)
            if v == vertex2: return True
            if v in visited: continue
            visited.add(v)
            queue.extend(self.neighbours[v])
        return False

if __name__ == '__main__':
    main()
