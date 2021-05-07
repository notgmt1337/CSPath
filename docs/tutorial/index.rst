Tutorial: Using CSPath
======================

Introduction To Shortest-Path Problems
--------------------------------------
Shortest-path problems are ubiquitous. An alarming number of the world's software would not be possible without shortest-path algorithms. To try and motivate why such software is needed: Imagine you are on vacation in Paris, France and would like to visit the Eiffel tower, starting from your hotel. You have purchased a map of Paris and you are trying to plan your way there. You quickly notice that there isn't just one route going from your hotel to the Eiffel tower, but rather a lot of them. Your next question is: What is, in terms of distance, the shortest such route?

This is basically what is called a "shortest-path problem". The keyword "shortest" need not refer to distance, but rather to the universal idea of cost. This interpretation is what abstractifies shortest-path algorithms and makes things such as friend-suggestions in Facebook possible. To formally introduce what a shortest-path problem is, we rely heavily on graph theory terminology. If your graph theory is a bit rusty, please visit the `bibliography`_ section.

Let :math:`G` be an edge-weighted graph and let :math:`S, E` be two nodes in :math:`G`. We need to find the path :math:`P` from :math:`S` to :math:`E` such that the weight-sum of the edges in :math:`P` is minimal. For small enough graphs, this isn't that much of a chore. However, it is virtually impossible to do this by hand for a graph corresponding to a city like London or New York. Thus, the solution is to develop algorithms that solve such problems and implement them for use within computer programs. 

Going back to the example above, you remember that there is a very handy app installed on your smartphone called `Google-Maps`_. You press on the 'Directions' button and input your hotel's address and 'Eiffel Tower, Paris, France' as your destination. And voilà, you have found the shortest-path. 

Installing CSPath
----------------------
Version 1.0.0 is not available for installation via pip, anaconda or others. Thus, the only way to install CSPath 1.0.0 is to download the source from GitHub (https://github.com/notgmt1337/CSPath) to your system.


Examples
--------
Two examples demonstrating the core functionality of CSPath are provided.

If a graph is given in the form of a `distance-matrix`_, we can calculate the shortest path as follows:

.. code-block:: python

    import numpy as np
    from cspath import Graph
    
    distance_matrix = np.array([[     0,      1, np.inf, np.inf, np.inf],
                                [np.inf,      0,      2,    1.5, np.inf],
                                [np.inf,      2,      0, np.inf,      4],
                                [np.inf, np.inf, np.inf,      0,    4.4],
                                [np.inf, np.inf, np.inf, np.inf,      0]])
    
    g = Graph(distance_matrix)
    
    print(g.ipq_dijkstra())
    print(g.a_star())
    print(g.bellman_ford())
    
    
    >>>(array([0., 1., 3., 4.]), 6.9, 0.0)
    >>>(array([0., 1., 3., 4.]), 6.9, 0.0)
    >>>(array([0., 1., 3., 4.]), 6.9, 0.0010001659393310547)
    
If the graph is described using a `coordinate`_ system, we can calculate the shortest path as follows:

.. code-block:: python

    import numpy as np
    from cspath import Graph
    
    g = Graph()
    
    g.addNode(0, 0, 0)
    g.addNode(-0.5, -1, 0)
    g.addNode(0.5, -1, 0)
    g.addNode(-0.5, -2, 0)
    g.addNode(0.5, -2, 0)
    g.addNode(0, -3, 0)
    
    g.linkNodes(0, 1, False)
    g.linkNodes(0, 2, False)
    g.linkNodes(1, 2, True)
    g.linkNodes(1, 3, True)
    g.linkNodes(1, 4, True)
    g.linkNodes(2, 3, True)
    g.linkNodes(2, 4, True)
    g.linkNodes(3, 4, True)
    g.linkNodes(3, 5, False)
    g.linkNodes(4, 5, False)
    
    
    print(g.dijkstra())
    print(g.a_star())
    print(g.floyd_warshall())
    
   >>>(array([0., 1., 3., 5.]), 3.23606797749979, 0.0)
   >>>(array([0., 1., 3., 5.]), 3.23606797749979, 0.0)
   >>>(array([0., 1., 3., 5.]), 3.23606797749979, 0.0)

Of course, there is the possibility to use a combination of the two methods.
    
.. _distance-matrix: https://cspath.readthedocs.io/en/latest/how-to/graph-parse.html#method-1-using-a-distance-matrix
.. _coordinate: https://cspath.readthedocs.io/en/latest/how-to/graph-parse.html#method-2-using-cartesian-coordinates
.. _bibliography: https://cspath.readthedocs.io/en/latest/reference/bibliography.html
.. _Google-Maps: https://www.google.com/maps
