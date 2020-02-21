# Graphs
Congratulations you've made it to graphs, the most complex data structures you will be
implementing in these kata. Graphs are conceptually made up of 2 structures, `Edges`, and
`Nodes`. `Nodes` are used to store data in the graph while `Edges` represent the
relationships between `Nodes`. For example you could represent a roadmap as a graph. In
this example city names like `Waco`, `Austin`, and `Dallas` would be nodes and highways
connecting the cities would be the edges. The graph might look like this.
```
[Austin] ---- [Waco] ---- [Dallas]
```

## Undirected Graphs
Undirected graphs are the simpler of the two types of graphs to represent and can be
visualized as shown in the diagram above. When a graph is undirected it means any `Edge`
between `Nodes` can be traversed both ways.

## Directed Graphs
Directed graphs are more complex because an `Edge` can only be traversed in a single
direction. To represent the same scenario as shown above the graph can be drawn with 2
directed edges between each `Node`. This allows for the same scenario in which there is a
path from `Ausin` to `Waco` as well as a path from `Waco` to `Austin`. The graph would
look something like this.
```
[Austin] <--> [Waco] <--> [Dallas]
```

To represent the scenario where there is only a path from `Austin` to `Waco` the graph
would be drawn like so.
```
[Austin] --> [Waco] <--> [Dallas]
```

## Djikstra's Algorithm
Djikatra's algorithm is a "Single Source Shortest Path" algorithm. This type of algorithm
is used to answer the question, "what is the shortest path between a source node and any
other node in the graph?" Instead of explaining the algorithm I recommend watching this
[video](https://www.youtube.com/watch?v=pVfj6mxhdMw) that does a far better job than I
could do. There are a few key points you should note before starting on your implementation.
 - Djikatra's Algorithm generates a minimum spanning tree from the source node to every other
    node in the graph
 - Edge weights must be positive.
 - The Distance from the source to itself is always 0.
 - You will need to keep track of 2 things while running Djikatra's
    - The nodes that have not been visited and
    - The lowest known path length for any nodes that have been discovered.
