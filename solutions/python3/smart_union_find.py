#!/usr/bin/python3
r"""
A solution using a smarter union-find data structure:

- component trees are kept somewhat balanced by always
  merging the smaller component into the bigger one; and
- path compression is used.
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
        # negative numbers are used at the roots of component trees
        # and give the number of vertices in the tree
        self.parents = {v: -1 for v in vertices}
        for v1, v2 in edges:
            self.union(v1, v2)

    def has_path_between(self, vertex1, vertex2):
        return self.find(vertex1) == self.find(vertex2)

    def find(self, vertex):
        parent = self.parents[vertex]
        if parent < 0:
            return vertex
        else:
            root = self.find(parent)
            # this is where path compression shows up
            self.parents[vertex] = root
            return root

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        size1 = -self.parents[root1]
        size2 = -self.parents[root1]
        if root1 != root2:
            # this is where trees are kept somewhat balanced
            if size1 < size2:
                self.parents[root1] = root2
                self.parents[root2] = -(size1 + size2)
            else:
                self.parents[root2] = root1
                self.parents[root1] = -(size1 + size2)

if __name__ == '__main__':
    main()
