Parse A Graph
=====================

Graph-parsing is essential to CSPath. Version 1.0.0 offers two methods of parsing graphs.

Method 1: Using a Distance Matrix
---------------------------------

Let :math:`n` denote the number of nodes in the graph.:raw-html:`<br />`The notation :math:`n_{1} \parallel n_{2}` means that node :math:`n_{1}` does not share an edge with node :math:`n_{2}`.:raw-html:`<br />`To denote the opposite, we use :math:`n_{1} \perp n_{2}`.:raw-html:`<br />`We define the distance function as follows:

.. math::
    d_{a, b} = d(n_{a}, n_{b}) = 
    \left\{
            \begin{array}{ll}
                  w(a, b) & \mbox{if } n_{a} \perp n_{b} \\
                  +\infty & \mbox{if } n_{a} \parallel n_{b}
            \end{array}
    \right.
, where :math:`w(a, b)` is the weight of the edge connecting nodes :math:`n_{a}, n_{b}`.


Method 2: Using Cartesian Coordinates
-------------------------------------
