Parse A Graph
=====================

Graph-parsing is essential to CSPath. Version 1.0.0 offers two methods of parsing graphs.

Method 1: Using a Distance Matrix
---------------------------------

Let :math:`n` denote the number of nodes in the graph. The notation :math:`n_{1} \parallel n_{2}` means that node :math:`n_{1}` does not share an edge with node :math:`n_{2}` and the notation :math:`n_{1} \perp n_{2}` means that node :math:`n_{1}` shares an edge with node :math:`n_{2}`. We define the distance function as follows:

.. math::
    d_{a, b} = d_{n_{a}, n_{b}} = 
    \left\{
            \begin{array}{ll}
                  w(a, b), if n_{a} \perp n_{b} \\
                  +\infty, if n_{a} \parallel n_{b}
            \end{array}
    \right.


Method 2: Using Cartesian Coordinates
-------------------------------------
