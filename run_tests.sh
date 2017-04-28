#!/bin/bash
set -o errexit -o nounset -o pipefail

run_test() {
    local name=$1
    local graph=$2
    local query=$3
    local expected=$4
    shift 4
    printf "Test $name: "
    if (cat "$graph" "$query" | "$@" | cmp "$expected" 2>/dev/null); then
        printf "succeeded!\n"
    else
        printf "failed!\n"
        return 1
    fi
}

time_run() {
    local name=$1
    local graph=$2
    local query=$3
    shift 3
    printf "Time test $name (10 iterations): "
    time for i in {1..10}; do cat "$graph" "$query" | "$@" >/dev/null; done
}

# A graph with 2 vertices and no edges
run_test 1 \
    data/p11.graph \
    data/v2.query \
    data/p11.expected \
    "$@"

# A graph with 2 vertices and 1 edge
run_test 2 \
    data/p2.graph \
    data/v2.query \
    data/p2.expected \
    "$@"

# A graph with 10 vertices:
# - all possible edges between vertices 0, 1, 2, 3, 4 are present
# - plus four edges to form the path 5 -- 9 -- 6 -- 8 -- 7
run_test 3 \
    data/k5p5.graph \
    data/v10.query \
    data/k5p5.expected \
    "$@"

# A graph with 1000 vertices and 500 edges
run_test 4 \
    data/sparse.graph \
    data/v1000.query \
    data/sparse.expected \
    "$@"

# A graph with 1000 vertices and 1000 edges
run_test 5 \
    data/medium.graph \
    data/v1000.query \
    data/medium.expected \
    "$@"

# A graph with 1000 vertices and 5000 edges
run_test 6 \
    data/dense.graph \
    data/v1000.query \
    data/dense.expected \
    "$@"

# Now the speed tests
for graph in sparse medium dense; do
    time_run "$graph" \
        data/"$graph".graph \
        data/v1000.query \
        "$@"
done
