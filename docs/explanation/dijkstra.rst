Dijkstra's Algorithm
====================

Dijkstra's shortest path algorithm is used for finding the shortest path from one node to another in edge-weighted graphs with positive weights. It is what is known as a `greedy`_ algorithm. The way it works, roughly, is the following:

- Step 1: With each node in the graph associate three variables, the distance from the start node, the node that was previously visited such that the path from the start node to the current node is the latter distance and whether the current node is visited or not. If a node is not an in-neighbor of the start node, the distance from the start node is infinity and the previous node is not defined.
- Step 2: Starting from the start node and for every unvisited node, find the unvisited node with the smallest distance from the current node and update the three variables. 

`This`_ video does a very good job of explaining Dijkstra's algorithm

There are 4 implementations of Dijkstra's shortest path algorithm available for use in CSPath. They are:

- :code:`cspath.Graph.dijkstra`
- :code:`cspath.Graph.ipq_dijkstra`
- :code:`cspath.Graph.dijkstra_all`
- :code:`cspath.Graph.ipq_dijkstra_all`

:code:`cspath.Graph.dijkstra` and :code:`cspath.Graph.ipq_dijkstra` are two different implementations of Dijkstra's algorithm that give the same output. The only difference lies in finding the nodes with the smallest distance. Please read the `previous`_ section for more information. 

:code:`cspath.Graph.dijkstra_all` and :code:`cspath.Graph.ipq_dijkstra_all` are equivalents, in the sense that they give the same `output`_. Again, the only difference lies in how the nodes with the smallest distance are found.



For more information, please visit https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm.


.. _greedy: https://en.wikipedia.org/wiki/Greedy_algorithm
.. _This: https://www.youtube.com/watch?v=pVfj6mxhdMw
.. _previous: https://cspath.readthedocs.io/en/latest/explanation/ipq.html
.. _output: https://cspath.readthedocs.io/en/latest/reference/source.html#cspath.Graph.Graph.dijkstra_all
