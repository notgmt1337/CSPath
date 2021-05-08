Indexed Priority Queue
======================

For a detailed explanation of IPQs, please visit https://mkhoshpa.github.io/IndexedPQ/.

CSPath makes extensive use of indexed priority queues, or IPQs for short. The motivation for using IPQs is to significantly lower the program runtime. In version 1.0.0, IPQs are used in functions :code:`cspath.Graph.ipq_dijkstra, cspath.Graph.ipq_dijkstra_all`. To see how the use of IPQs speeds up the program, we need to consider two pieces of code: `one`_, `two`_. This explanation relies heavily on `Dijkstra's`_ algorithm.

A very important step in Dijkstra's algorithm is finding the unvisited node with the smallest positive distance from the current node that is visited. As you can see for yourself, the first implementation of Dijkstra's algorithm, uses 2 :code:`for` loops to achieve that. On average, the time-complexity of this is :math:`O(n^2)`, since we first have to find an unvisited node, and then from all the unvisited nodes we need to find the one with the smallest positive distance. The second implementation of Dijkstra uses ipqs in a very cunning way. The elements with the highest priority in the IPQ are the unvisited nodes with the smallest positive distance from the current node. Thus, to get the required node for the continuation of the algorithm, one only has to 'pop' the item from the list, which has time-complexity :math:`O(logn)`. This is a significant difference, which becomes a lot more apparent as :math:`n \to + \infty`.


.. _one: https://cspath.readthedocs.io/en/latest/_modules/cspath/Graph.html#Graph.dijkstra
.. _two: https://cspath.readthedocs.io/en/latest/_modules/cspath/Graph.html#Graph.ipq_dijkstra
.. _Dijkstra's: https://cspath.readthedocs.io/en/latest/explanation/dijkstra.html
