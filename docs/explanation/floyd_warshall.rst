Floyd-Warshall Algorithm
========================

The Floyd-Warshall algorithm is a shortest path algorithm capable of finding the shortest path from a start node to an end node in edge-weighted graphs with positive or negative weights and no negative cycles. The time-complexity for the Floyd-Warshall algorithm is :math:`O(|V|^3)`, where :math:`|V|` is the number of the nodes in the graph. This makes the algorithm slower than Dijkstra's algorithm and the A* algorithm. There are two steps to the algorithm and for a concrete explanation, we will consider them both. 


Step 1
------

.. code-block:: python

        M = np.array([0], dtype = np.float64)
        M = np.resize(M, (numNodes, numNodes))

        prev = np.array([0], dtype = np.int64)
        prev = np.resize(prev, (numNodes, numNodes))

        for i in np.arange(numNodes):
            for j in np.arange(numNodes):
                if i == j:
                    M[i][j] = 0
                    prev[i][j] = i
                if self.__distMatrix[i][j] < 0:
                    M[i][j] = np.inf
                    prev[i][j] = -1
                else:
                    M[i][j] = self.__distMatrix[i][j]
                    prev[i][j] = j

This part essentially sets up the arrays that are necessary for the initialization part of the graph. The array :code:`M` holds the shortest routes between every two nodes, a copy of the distance matrix. The array :code:`prev` holds the previous nodes for every path corresponding to an entry in :code:`M`. This is exactly the same technique as in Dijkstra's algorithm, it is just extended to facilitate the finding of the shortest route from any node to any other node.

Step 2
------

.. code-block:: python

        for k in np.arange(numNodes):
            for i in np.arange(numNodes):
                for j in np.arange(numNodes):
                    if M[i][j] > M[i][k] + M[k][j]:
                        M[i][j] = M[i][k] + M[k][j]
                        prev[i][j] = prev[i][k] 

This step is essentially repeated 'edge-relaxation', where we loop through all the nodes in the distance matrix :code:`M` and we check whether the shortest route from node :code:`i` to node :code:`j` can be shortened by visiting another node :code:`k`. If so, the arrays are updated. After the loops finish, we are guaranteed to have the shortest routes between any two nodes.


In CSPath, the only available implementation of the Floyd-Warshall algorithm is :code:`cspath.Graph.floyd_warshall`.
For more information, please visit this `article`_ in Wikipedia.


.. _article: https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm
