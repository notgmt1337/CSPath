Parse A Graph
=====================

Graph-parsing is essential to CSPath. Version 1.0.0 offers two methods of parsing graphs.

Let :math:`m` denote the number of nodes in the graph. We introduce some notation that will help us encode the directedness of graphs.

We use:

- :math:`n_{1} \parallel n_{2}`, if one cannot go from node :math:`n_{1}` to node :math:`n_{2}` by following only one edge.
- :math:`n_{1} \perp n_{2}`, if one can go from node :math:`n_{1}` to node :math:`n_{2}` by following one edge.

Note that:

1. :math:`n_{1} \parallel n_{2}` does not imply that :math:`n_{1}, n_{2}` do not share an edge and thereby :math:`n_{2} \parallel n_{1}`, as there could exist a directed edge from :math:`n_{2}` to :math:`n_{1}`.
2. :math:`n_{1} \perp n_{2}` does not imply :math:`n_{2} \perp n_{1}`, as the edge connecting the two could be directed from :math:`n_{1}` to :math:`n_{2}`.


Method 2: Using a Distance Matrix
---------------------------------

We define the distance function as follows.

.. math::
    d_{a, b} = d(n_{a}, n_{b}) = 
                                 \left\{
                                        \begin{array}{ll}
                                              w(a, b) & \mbox{if } n_{a} \perp n_{b} \\
                                              +\infty & \mbox{if } n_{a} \parallel n_{b}
                                        \end{array}
                                 \right.
                                    
                                
, where :math:`w(a, b)` is the weight of the edge connecting nodes :math:`n_{a}, n_{b}`.  

As a convention, :math:`n_{0}` is the start node and :math:`n_{m-1}` is the end node.
The distance matrix is the square matrix with entries the values of the distance function in the following manner:

.. math::
    D =
        \begin{pmatrix}
              0          & d_{0, 1}   & d_{0, 2}     & ...    & d_{0, m-2}   & d_{0, m-1} \\
              d_{1, 0}   & 0          & d_{1, 2}     & ...    & d_{1, m-2}   & d_{1, m-1} \\
              d_{2, 0}   & d_{2, 1}   & 0            & ...    & d_{2, m-2}   & d_{2, m-1} \\
                         &            &              & \ddots &              &            \\
              d_{m-2, 0} & d_{m-2, 1} & d_{m-2, 2}   & ...    & 0            & d_{m-2, m-1} \\
              d_{m-1, 0} & d_{m-1, 1} & d_{m - 1, 2} & ...    & d_{m-1, m-2} & 0
        \end{pmatrix}
        
       
A consequence of the definition of the distance matrix and our notation is that :math:`d_{a, b} = d_{b, a}` is not necessarily true. This means that our distance matrix can describe any graph, be it directed or undirected.
In code, the distance matrix must always be of type :code:`numpy.array` and the first and last rows must correspond to the start and end nodes, respectively. 

To make things clearer, consider the graph below.



Method 2: Using Cartesian Coordinates
-------------------------------------

Using Cartesian coordinates
