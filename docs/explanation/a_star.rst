A* Algorithm
============

The A* Algorithm is an extension of `Dijkstra's`_ algorithm. The only difference is that the A* algorithm has its own system of prioritizing which unvisited nodes to visit first. As you might know, the equivalent criterion in Dijkstra is basically the distance from the current node. However, in A* this criterion is the distance from the current node plus a quantity called a 'heuristic'. The heuristic function associates with each node its distance from the start node.


For more information, please visit: https://en.wikipedia.org/wiki/A*_search_algorithm. 

.. _Dijkstra's: https://cspath.readthedocs.io/en/latest/explanation/dijkstra.html
