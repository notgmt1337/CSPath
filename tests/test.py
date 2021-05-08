import numpy as np
import cspath as csp


"""
Graph taken from: http://people.brunel.ac.uk/~mastjjb/jeb/or/gt91.gif

The shortest path from A to G is (A, C, E, G) = (0, 2, 4, 6)
Shortest path length = 8

"""

tMatrix = np.array([
      [     0,      5,      1,      3, np.inf, np.inf, np.inf],
      [     5,      0, np.inf,      4, np.inf,      6, np.inf],
      [     1, np.inf,      0,      2,      3, np.inf, np.inf],
      [     3,      4,      2,      0,      7,      9, np.inf],
      [np.inf, np.inf,      3,      7,      0, np.inf,      4],
      [np.inf,      6, np.inf,      9, np.inf,      0,      5],
      [np.inf, np.inf, np.inf, np.inf,      4,      5,      0]
])

"""
For explanations about each of these methods that are tested, please visit
https://cspath.readthedocs.io/en/latest/reference/source.html
"""


def test_IsValidDistanceMatrix():

      """
      This code tests function cspath.Graph.Graph.IsValidDistanceMatrix
      """

      #Valid distance matrix
      dm1 = np.array([
            [0, 1, 2, 3],
            [1, 0, 4, 5],
            [2, 4, 0, 6],
            [3, 5, 6, 0],
      ])

      #Invalid distance matrix: 0 entry not on main diagonal
      dm2 = np.array([
            [0, 0],
            [1, 0]
      ])

      #Invalid distance matrix: main diagonal entry not 0
      dm3 = np.array([
            [1, 0],
            [0, 1]
      ])

      #Invalid distance matrix: invalid entries
      dm4 = np.array([
            [0, "words"],
            [3, 0]
      ])

      #Invalid distance matrix: invalid type
      dm5 = [
            [0, 2],
            [3, 0],
      ]

      g = csp.Graph()

      assert g.IsValidDistanceMatrix(dm1)
      assert not g.IsValidDistanceMatrix(dm2)
      assert not g.IsValidDistanceMatrix(dm3)
      assert not g.IsValidDistanceMatrix(dm4)
      assert not g.IsValidDistanceMatrix(dm5)

def test_a_star():

      """
      This code tests function cspath.Graph.Graph.a_star
      """
      
      g = csp.Graph(tMatrix)      

      result = g.a_star()

      assert np.array_equal(result[0], np.array([0, 2, 4, 6]))
      assert result[1] == 8

def test_addNode():
      
      
      """
      This code tests function cspath.Graph.Graph.addNode
      """

      g = csp.Graph()

      n1 = g.addNode(2, 3, 4)
      n2 = g.addNode(4, 5, 6)
      n3 = g.addNode(2, 3, 4)

      assert np.array_equal(g.getNodeList(), np.array([n1, n2]))

def test_bellman_ford():

      """
      This code tests function cspath.Graph.Graph.bellman_ford
      """

      g = csp.Graph(tMatrix)      

      result = g.bellman_ford()

      assert np.array_equal(result[0], np.array([0, 2, 4, 6]))
      assert result[1] == 8


def test_bellman_ford_all():

      """
      This code tests function cspath.Graph.Graph.bellman_ford_all
      """
      
      g = csp.Graph(tMatrix)      

      result = g.bellman_ford_all()

      assert np.array_equal(result[0], np.array([0, 5, 1, 3, 4, 11, 8]))
      assert np.array_equal(result[1], np.array([0, 0, 0, 0, 2, 1, 4]))
      assert np.array_equal(result[2], np.array([0, 2, 4, 6]))
      assert result[3] == 8

def test_changeNode():
      
      """
      This code tests function cspath.Graph.Graph.changeNode
      """

      g = csp.Graph()

      g.addNode(100, 100, 100)
      g.addNode(300, 200, 400)
      g.addNode(700, 200, 50)

      g.changeNode(1, 45, 55, 65)

      assert np.array_equal(g.getNodeList()[1].get(), np.array([45, 55, 65]))

def test_delLink():
      
      """
      This code tests function cspath.Graph.Graph.delLink
      """

      g = csp.Graph()

      g.addNode(100, 100, 100)
      g.addNode(200, 200, 200)
      g.addNode(200, 300, 300)
      
      g.linkNodes(0, 1, True)
      g.linkNodes(1, 2, False)
      g.linkNodes(0, 2, True)

      """
      After this, the internal distance matrix should look like
      [     0,     d01, d02],
      [   d10,       0, d12],
      [   d20, -np.inf,   0],
      """

      g.delLink(0, 1, False)
      g.delLink(0, 2, True)

      """
      After this, the internal distance matrix should look like
      [      0, -np.inf, -np.inf],
      [    d10,       0,     d12],
      [-np.inf, -np.inf,       0],
      """

      d10 = np.linalg.norm(np.array([100, 100, 100]) - np.array([200, 200, 200]))
      d12 = np.linalg.norm(np.array([200, 200, 200]) - np.array([200, 300, 300]))

      edm = np.array([
            [      0, -np.inf, -np.inf],
            [    d10,       0,     d12],
            [-np.inf, -np.inf,       0]
      ])

      assert np.array_equal(g.getDistanceMatrix(), edm)



def test_dijkstra():

      """
      This code tests function cspath.Graph.Graph.dijkstra
      """

      g = csp.Graph(tMatrix)      

      result = g.dijkstra()

      assert np.array_equal(result[0], np.array([0, 2, 4, 6]))
      assert result[1] == 8

def test_dijkstra_all():
      
      """
      This code tests function cspath.Graph.Graph.dijkstra_all
      """
      
      g = csp.Graph(tMatrix)      

      result = g.dijkstra_all()

      assert np.array_equal(result[0], np.array([0, 5, 1, 3, 4, 11, 8]))
      assert np.array_equal(result[1], np.array([0, 0, 0, 0, 2, 1, 4]))
      assert np.array_equal(result[2], np.array([0, 2, 4, 6]))
      assert result[3] == 8

def test_floyd_warshall():

      g = csp.Graph(tMatrix)      

      result = g.floyd_warshall()

      assert np.array_equal(result[0], np.array([0, 2, 4, 6]))
      assert result[1] == 8 

def test_get3DMode():
      
      """
      This code tests function cspath.Graph.Graph.get3DMode
      """

      dm1 = np.array([
            [0, 1],
            [1, 0]
      ])

      g1 = csp.Graph(dm1)

      g2 = csp.Graph()
      g3 = csp.Graph()

      g2.addNode(1, 2, 0)
      g2.addNode(3, 4, 0)

      g3.addNode(1, 2, 1)
      g3.addNode(1, 2, 0)

      assert g1.get3DMode() is None
      assert not g2.get3DMode()
      assert g3.get3DMode()

def test_getCoordinateMode():

      """
      This code tests function cspath.Graph.Graph.getCoordinateMode
      """

      dm1 = np.array([
            [0, 1],
            [1, 0]
      ])

      g1 = csp.Graph(dm1)

      g2 = csp.Graph()
      g2.addNode(100, 100, 100)

      assert not g1.getCoordinateMode()
      assert g2.getCoordinateMode()

def test_getDistanceMatrix():

      """
      This code tests function cspath.Graph.Graph.getDistanceMatrix
      """

      dm1 = np.array([
            [0, 1],
            [1, 0]
      ])

      g = csp.Graph(dm1)

      assert np.array_equal(g.getDistanceMatrix(), dm1)

def test_getNodeList():

      """
      This code tests function cspath.Graph.Graph.getNodeList
      """

      g = csp.Graph()

      n1 = csp.addNode(100, 200, 300)
      n2 = csp.addNode(500, 500, 500)

      assert np.array_equal(g.getNodeList(), np.array([[100, 200, 300], [500, 500, 500]]))

def test_get_idegree():

      """
      This code tests function cspath.Graph.Graph.get_idegree
      """

      mtrx = np.array([
            [     0, np.inf,      1,      3, np.inf, np.inf, np.inf],
            [     5,      0, np.inf,      4, np.inf,      6, np.inf],
            [     1, np.inf,      0,      2,      3, np.inf, np.inf],
            [     3,      4,      2,      0,      7,      9, np.inf],
            [np.inf, np.inf,      3,      7,      0, np.inf,      4],
            [np.inf,      6, np.inf,      9, np.inf,      0,      5],
            [np.inf, np.inf, np.inf, np.inf,      4,      5,      0]
      ])

      g = csp.Graph(mtrx)

      assert g.get_idegree(0) == 3
      assert g.get_idegree(3) == 5


def test_get_ineighbors():
      
      """
      This code tests function cspath.Graph.Graph.get_ineighbors
      """

      mtrx = np.array([
            [     0, np.inf,      1,      3, np.inf, np.inf, np.inf],
            [     5,      0, np.inf,      4, np.inf,      6, np.inf],
            [     1, np.inf,      0,      2,      3, np.inf, np.inf],
            [     3,      4,      2,      0,      7,      9, np.inf],
            [np.inf, np.inf,      3,      7,      0, np.inf,      4],
            [np.inf,      6, np.inf,      9, np.inf,      0,      5],
            [np.inf, np.inf, np.inf, np.inf,      4,      5,      0]
      ])

      g = csp.Graph(mtrx)

      assert np.array_equal(g.get_ineighbors(0), np.array([1, 2, 3]))
      assert np.array_equal(g.get_ineighbors(1), np.array([3, 5]))

def test_get_odegree():

      """
      This code tests function cspath.Graph.Graph.get_odegree
      """

      mtrx = np.array([
            [     0, np.inf,      1,      3, np.inf, np.inf, np.inf],
            [     5,      0, np.inf,      4, np.inf,      6, np.inf],
            [     1, np.inf,      0,      2,      3, np.inf, np.inf],
            [     3,      4,      2,      0,      7,      9, np.inf],
            [np.inf, np.inf,      3,      7,      0, np.inf,      4],
            [np.inf,      6, np.inf,      9, np.inf,      0,      5],
            [np.inf, np.inf, np.inf, np.inf,      4,      5,      0]
      ])

      g = csp.Graph(mtrx)

      assert g.get_odegree(0) == 2
      assert g.get_odegree(4) == 3

def test_get_oneighbors():

      """
      This code tests function cspath.Graph.Graph.get_ineighbors
      """

      mtrx = np.array([
            [     0, np.inf,      1,      3, np.inf, np.inf, np.inf],
            [     5,      0, np.inf,      4, np.inf,      6, np.inf],
            [     1, np.inf,      0,      2,      3, np.inf, np.inf],
            [     3,      4,      2,      0,      7,      9, np.inf],
            [np.inf, np.inf,      3,      7,      0, np.inf,      4],
            [np.inf,      6, np.inf,      9, np.inf,      0,      5],
            [np.inf, np.inf, np.inf, np.inf,      4,      5,      0]
      ])

      g = csp.Graph(mtrx)

      assert np.array_equal(g.get_oneighbors(0), np.array([2, 3]))
      assert np.array_equal(g.get_oneighbors(1), np.array([0, 3, 5]))


def test_ipq_dijkstra():

      """
      This code tests function cspath.Graph.Graph.ipq_dijkstra
      """

      g = csp.Graph(tMatrix)      

      result = g.ipq_dijkstra()

      assert np.array_equal(result[0], np.array([0, 2, 4, 6]))
      assert result[1] == 8

def test_ipq_dijkstra_all():
   
      """
      This code tests function cspath.Graph.Graph.ipq_dijkstra_all
      """
      
      g = csp.Graph(tMatrix)      

      result = g.ipq_dijkstra_all()

      assert np.array_equal(result[0], np.array([0, 5, 1, 3, 4, 11, 8]))
      assert np.array_equal(result[1], np.array([0, 0, 0, 0, 2, 1, 4]))
      assert np.array_equal(result[2], np.array([0, 2, 4, 6]))
      assert result[3] == 8 

def test_linkNodes():
      
      """
      This code tests function cspath.Graph.Graph.linkNodes
      """
      
      g1 = csp.Graph()

      g1.addNode(100, 100, 100)
      g1.addNode(200, 200, 200)

      g2 = csp.Graph()
      
      g2.addNode(300, 300, 300)
      g2.addNode(600, 600, 600)

      g3 = csp.Graph()
      
      g3.addNode(400, 400, 400)
      g3.addNode(800, 800, 800)

      """
      After this, the interal distance matrix for g1, g2 & g3 should be 
      [0, -np.inf],
      [-np.inf, 0]
      """

      g1.linkNodes(0, 1, False)
      g2.linkNodes(0, 1, True)
      g3.linkNodes(1, 0, False)
      
      """
      After this, the interal distance matrix for g1, g2 & g3 should be 
      [      0, d01],
      [-np.inf,   0]

      [      0, d01],
      [    d10,   0]

      [      0, -np.inf],
      [    d10,       0]
      """

      d1 = np.linalg.norm(np.array([100, 100, 100] - np.array([200, 200, 200])))
      d2 = np.linalg.norm(np.array([300, 300, 300] - np.array([600, 600, 600])))
      d3 = np.linalg.norm(np.array([400, 400, 400] - np.array([800, 800, 800])))
      
      dm1 = np.array([
            [      0, d1],
            [-np.inf,  0]
      ])

      dm2 = np.array([
            [      0, d2],
            [     d2,  0]
      ])

      dm3 = np.array([
            [      0, -np.inf],
            [     d3,       0]
      ])

      assert np.array_equal(g1.getDistanceMatrix(), dm1)
      assert np.array_equal(g2.getDistanceMatrix(), dm2)
      assert np.array_equal(g3.getDistanceMatrix(), dm3)

def test_setDistanceMatrix():
      
      """
      This code tests function cspath.Graph.Graph.setDistanceMatrix
      """
      
      #Valid distance matrix
      dm1 = np.array([
            [0, 1, 2, 3],
            [1, 0, 4, 5],
            [2, 4, 0, 6],
            [3, 5, 6, 0],
      ])

      #Invalid distance matrix: 0 entry not on main diagonal
      dm2 = np.array([
            [0, 0],
            [1, 0]
      ])

      #Invalid distance matrix: main diagonal entry not 0
      dm3 = np.array([
            [1, 0],
            [0, 1]
      ])

      #Invalid distance matrix: invalid entries
      dm4 = np.array([
            [0, "words"],
            [3, 0]
      ])

      #Invalid distance matrix: invalid type
      dm5 = [
            [0, 2],
            [3, 0],
      ]

      g = csp.Graph()

      assert g.setDistanceMatrix(dm1)
      assert not g.setDistanceMatrix(dm2)
      assert not g.setDistanceMatrix(dm3)
      assert not g.setDistanceMatrix(dm4)
      assert not g.setDistanceMatrix(dm5)

def test_NodeGet():
      
      """
      This code tests function cspath.Node.Node.NodeGet
      """
      
      n1 = csp.Node(245, 235, 225)
      
      assert np.array_equal(n1.get(), np.array([245, 235, 225]))

def test_setNode():

      """
      This code tests function cspath.Node.Node.setNode
      """

      n1 = csp.Node(100, 100, 100)
      n1.setNode(200, 300, 400)

      assert np.array_equal(n1.get(), np.array([200, 300, 400]))

def test_setX():

      """
      This code tests function cspath.Node.Node.setX
      """

      n1 = csp.Node(100, 100, 100)
      n1.setX(30)

      assert n1.get()[0] == 30

def test_setY():

      """
      This code tests function cspath.Node.Node.setY
      """

      n1 = csp.Node(100, 100, 100)
      n1.setY(30)

      assert n1.get()[1] == 30

def test_setZ():

      """
      This code tests function cspath.Node.Node.setZ
      """

      n1 = csp.Node(100, 100, 100)
      n1.setZ(30)

      assert n1.get()[2] == 30
      

def test_nodeEq():

      """
      This code tests function cspath.Node.nodeEq
      """

      n1 = csp.Node(100, 100, 100)
      n2 = csp.Node(100, 100, 100)
      n3 = csp.Node(300, 100, 100)

      assert csp.nodeEq(n1, n2)
      assert not csp.nodeEq(n1, n3)

def test_nodeInList():

      """
      This code tests function cspath.Node.nodeInList
      """
      
      n1 = csp.Node(100, 100, 100)
      n2 = csp.Node(100, 100, 100)
      n3 = csp.Node(100, 100, 101)

      nList = np.array([n1])

      assert csp.nodeInList(n2, nList)
      assert not csp.nodeInList(n3, nList)




test_get_idegree()
test_get_ineighbors()
test_get_odegree()
test_get_oneighbors()
test_ipq_dijkstra_all()
test_bellman_ford_all()
test_dijkstra_all()
test_ipq_dijkstra()
test_floyd_warshall()
test_dijkstra()
test_bellman_ford()
test_a_star()
test_IsValidDistanceMatrix()
test_getDistanceMatrix()
test_getCoordinateMode()
test_setDistanceMatrix()
test_changeNode()
test_delLink()
test_get3DMode()
test_NodeGet()
test_addNode()
test_linkNodes()
test_setNode()
test_setX()
test_setY()
test_setZ()
test_nodeEq()
test_nodeInList()
