Compute The Shortest Path
=========================

The first thing to do is `choose`_ which algorithm you want to use, then all you'd have to do is call the corresponding function.

Let us revisit the examples from the `parsing`_ section:

Example 1
---------

We use the :code:`cspath.Graph.ipq_dijkstra` and :code:`cspath.Graph.bellman_ford` functions. The shortest path can be computed in the following way:

.. code-block:: python

    import numpy as np
    from cspath import Graph
    distance_matrix = np.array([[     0,       1,  np.inf,  np.inf,  np.inf,  np.inf,  np.inf,  np.inf], 
                                [     1,       0,     1.2,     1.3,     1.5,  np.inf,  np.inf,  np.inf],
                                [np.inf,     1.2,       0,  np.inf,     0.3,     1.1,  np.inf,  np.inf], 
                                [np.inf,     1.3,  np.inf,       0,     0.6,  np.inf,  np.inf,       2], 
                                [np.inf,  np.inf,  np.inf,  np.inf,       0,     0.1,     1.0,     1.1], 
                                [np.inf,  np.inf,     1.1,  np.inf,     0.1,       0,     0.5,  np.inf], 
                                [np.inf,  np.inf,  np.inf,  np.inf,       1,     0.5,       0,     0.7], 
                                [np.inf,  np.inf,  np.inf,  np.inf,     1.1,  np.inf,     0.7,       0],
                              ])
                              
    g = Graph(distance_matrix)
    print(g.ipq_dijkstra())
    print(g.bellman_ford())
    
    >>>(array([0., 1., 4., 7.]), 3.6, 0.001149892807006836)
    >>>(array([0., 1., 4., 7.]), 3.6, 0.0)

:code:`array([0., 1., 4., 7.])` corresponds to the actual shortest path (Node 0 to 1 to 4 to 7), :math:`3.6` is the length of the path in distance units and :math:`0.001149892807006836, 0.0` are the algorithm runtimes.

.. _choose: https://cspath.readthedocs.io/en/latest/explanation/index.html
.. _parsing: https://cspath.readthedocs.io/en/latest/how-to/graph-parse.html

Example 2
---------

We use the :code:`cspath.Graph.a_star` and :code:`cspath.Graph.floyd_warshall` functions. The shortest path can be computed by:

.. code-block:: python

    from cspath import Graph
    
    g = Graph()
    
    n0 = g.addNode(0, 0, 0)
    n1 = g.addNode(-1, -1, 0)
    n2 = g.addNode( 1, -1, 0)
    n3 = g.addNode(-1.5, -2, 0)
    n4 = g.addNode(-0.5, -2, 0)
    n5 = g.addNode(0.5, -2, 0)
    n6 = g.addNode(1.5, -2, 0)
    
    g.linkNodes(0, 1, False)
    g.linkNodes(0, 2, False)
    g.linkNodes(1, 3, True)
    g.linkNodes(1, 4, True)
    g.linkNodes(1, 5, True)
    g.linkNodes(2, 5, False)
    g.linkNodes(2, 6, True)
    g.linkNodes(3, 2, False)
    g.linkNodes(4, 5, False)
    g.linkNodes(5, 6, False)
    
    print(g.a_star())
    print(g.floyd_warshall())
    
    >>>(array([0., 2., 6.]), 2.53224755112299, 0.0009970664978027344)
    >>>(array([0., 2., 6.]), 2.53224755112299, 0.0007607936859130859)
    
