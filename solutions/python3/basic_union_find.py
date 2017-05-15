#!/usr/bin/python3
r"""
A solution using a naive union-find data structure:

- no care is taken to keep component trees balanced; and
- path compression is not used.
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
        self.parents = {v: v for v in vertices}
        for v1, v2 in edges:
            self.union(v1, v2)

    def has_path_between(self, vertex1, vertex2):
        return self.find(vertex1) == self.find(vertex2)

    def find(self, vertex):
        parent = self.parents[vertex]
        if parent == vertex:
            return vertex
        else:
            return self.find(parent)

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        self.parents[root1] = root2

if __name__ == '__main__':
    main()
