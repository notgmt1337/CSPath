A* Algorithm
============

The A* Algorithm is an extension of `Dijkstra's`_ algorithm. The only difference is that the A* algorithm has its own system of prioritizing which unvisited nodes to visit first. As you might know, the equivalent criterion in Dijkstra is basically the distance from the start node to the currently-considered node. However, in A* this criterion is previous distance plus a quantity called a 'heuristic'. The heuristic function associates with each node its distance from the start node. To clarify, let us consider the following code snippets:

1. A*
-----

.. code-block:: python

    min_idx = 1

    for j in np.arange(2, numNodes):
        if heur[j] + shrDist[j] < heur[min_idx] + shrDist[min_idx] and not vis[j]:
            min_idx = j

2. Dijkstra's
-------------

.. code-block:: python

    min_idx = 1

    for j in np.arange(2, numNodes):
        if shrDist[j] < shrDist[min_idx] and not vis[j]:
            min_idx = j

As you see, these two pieces of code perform the same function: finding the unvisited node with the highest priority, that is, the unvisited node with the least overall score. In Dijkstra's algorithm, the score is just the distance from the start node to the node in question (:code:`shrDist[j]`). In A*, that score is equal to :code:`shrDist[j] + heur[j]`, the shortest distance from the start node to the node in question plus the heuristic. A very good heuristic has the potential of significantly lowering the execution time of the algorithm. Because of this specific reason, GPS systems usually implement the A* algorithm, rather than the Dijkstra. The heuristic that is normally used in such cases is the `euclidean`_ distance or the `spherical`_ distance between two points. However, there really is no limitation to what the heuristic can be.

In CSPath, the A* algorithm is used with the euclidean distance between two points as a heuristic. This requires the nodes to be described using coordinates, rather than just a distance matrix. This implementation of A* in CSPath is :code:`cspath.Graph.a_star`. 

For more information, please visit: https://en.wikipedia.org/wiki/A*_search_algorithm. 


.. _euclidean: https://en.wikipedia.org/wiki/Euclidean_distance
.. _spherical: https://en.wikipedia.org/wiki/Great-circle_distance

.. _Dijkstra's: https://cspath.readthedocs.io/en/latest/explanation/dijkstra.html
