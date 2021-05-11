Bellman-Ford Algorithm
======================

The Bellman-Ford algorithm is a shortest path algorithm that can handle graphs with negative edge-weights, unlike Dijsktra's. The main problem with the Bellman-Ford algorithm is that it is very slow compared to Dijkstra, for the same configuration. The time-complexity for the Bellman-Ford is :math:`O(|V| \cdot |E|)`, where :math:`|V|` and :math:`|E|` are the number of nodes and edges, respectively. 

Just like most shortest path algorithms, the Bellman-Ford algorithm proceeds by relaxation, overestimating the distance between two nodes until a smaller estimate arises. There are 3 steps to the Bellman-Ford algorithm. To give a solid explanation, we use the `source`_ code: 


Step 1
------

.. code-block:: python

        numNodes = len(self.__distMatrix)

        if numNodes == 0:
            return None, None, None

        start = time()

        shr = np.array([], dtype = np.float64)

        prev = np.array([], dtype = np.int64)

        for i in np.arange(numNodes):
            if self.__distMatrix[0][i] != -np.inf:
                shr = np.append(shr, self.__distMatrix[0][i])
                prev = np.append(prev, 0)
            else:
                shr = np.append(shr, np.inf)
                prev = np.append(prev, -1)    

This step initializes the graph. The :code:`shr` array keeps the length of the shortest routes from the start node to each other node and the :code:`prev` array stores the corresponding previous node for each route in :code:`shr`, exactly like `Dijkstra's`_ algorithm. For every node, we check if it is an out-neighbor of the start node, if it is, we update the :code:`shr` and :code:`prev` arrays accordingly. If not, the distance from the node to the start node is infinity and the previous node is not defined. 

Step 2
------

.. code-block:: python

        for i in np.arange(1, numNodes):
            
            for a in np.arange(numNodes):
                for b in np.arange(numNodes):

                    if a != b and self.__distMatrix[a][b] != -np.inf:
                        if self.__distMatrix[a][b] + shr[a] <  shr[b]:
                            shr[b] = self.__distMatrix[a][b] + shr[a]
                            prev[b] = a
        end = time()

In this step, we perform edge-relaxation :math:`|V|` times, for every pair of nodes. This is how the shortest paths are calculated.

Step 3
------

.. code-block:: python

        for a in np.arange(numNodes):
            for b in np.arange(numNodes):

                if a != b and self.__distMatrix[a][b] + shr[a] < shr[b] and self.__distMatrix[a][b] != -np.inf:
                    return None, "Detected Negative Cycle", end - start

The final step is negative cycle detection. Basically, if there is a cycle such that after you follow it your collective cost is less than when you started following it, then you could repeat this infinitely many times to make your total cost infinitely small. This cannot be allowed. So, we need to do negative cycle detection, which determines whether somewhere in the graph, there exists such a negative cycle.


.. _Dijkstra's: https://cspath.readthedocs.io/en/latest/explanation/dijkstra.html


For more information, please visit this `article`_ on Wikipedia. 

.. _article: https://en.wikipedia.org/wiki/Bellman–Ford_algorithm


.. _source: https://cspath.readthedocs.io/en/latest/_modules/cspath/Graph.html#Graph.bellman_ford
