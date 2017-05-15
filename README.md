# Exercise: find connected components of a graph

This repo contains:

- a small test suite;
- a garbage benchmark suite;
- an implementation stub called `stub.py`; and
- a few implemented solutions in the `solutions` directory.

If you don't want any spoilers for now, _don't look in the `solutions` directory_.
Also, _don't look at [the Wikipedia page for this problem](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)_.

## Problem statement

Your program is given a description of a graph and some connectivity queries about this graph on standard input, for example:

```
3
1
0 2
4
0 1
1 2
2 0
0 0
```

- The first line lists the number *V* of vertices of your graph.
  The vertices are labelled by increasing integers
  starting from 0 and ending with *V*-1.
  In the example there are `3` vertices, labelled `0, 1, 2`.
- The second line lists the number *E* of edges of your graph.
  In the example there is only `1` edge.
- The next *E* lines contain the edges of the graph,
  which are pairs of distinct vertices separated by a space.
  In the example there is an edge between vertices `0` and `2`.
- The next line lists the number *Q* of connectivity queries.
  In the example there are `4` queries.
- The next *Q* lines contain the queries,
  which are pairs of (possibly equal) vertices separated by a space.
  The query `v1 v2` asks **whether there is a path in the graph**
  which joins the vertices `v1` and `v2`, and the answer is either
  `yes` (they are connected by a path) or
  `no` (they are not connected by a path).

In the example, the correct answer to print on standard output would be:

```
no
no
yes
yes
```

## Running the tests

If you like python you can use the file `stub.py` as a starting point, which takes care of the input and output handling. Otherwise use whatever language you prefer, since the test suite doesn't care.

Once you have an implementation, you can test it by running the script:

```bash
./run_tests.sh ./stub.py
```

If you want to see how well my intended solution does, you can test it by running:

```bash
./run_tests.sh solutions/python3/smart_union_find.py
```

This will run:

- 3 tests on small graphs (2, 2 and 10 vertices)
- 3 tests on bigger graphs (1000 vertices with 500, 1000 and 5000 edges), and then
- a speed test on each of the bigger graphs.

## What next?

Try to use your graph connectivity algorithm skills on [Project Euler problem 107](https://projecteuler.net/problem=107)!

Also possibly now you could look at the provided solutions, compare them with yours, and run the speed tests on them.
