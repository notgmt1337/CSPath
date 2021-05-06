"""Graph class for CSPath"""
#########################
#       IMPORTS         #
#########################
import numpy as np
from time import time
from . import Node as nd
######################################
#            GRAPH CLASS             #
######################################

class Graph:
    """
    Initializes instance of the :code:`cspath.Graph` class
    
    Parameters
    ----------
    
        distanceMatrix: numpy.array, optional
    
    If no distanceMatrix is given or the distanceMatrix given is invalid, 
    the distanceMatrix of the class will not be initialized
    """
    def __init__(self, distanceMatrix = None):

        self.__distMatrix = np.array([], dtype = np.ndarray)
        self.__NodeList = None
        self.__3D = False
        self.__coordinateMode = False

        if isinstance(distanceMatrix, np.ndarray):
            
            if self.checkDistanceMatrix(distanceMatrix):

                self.__distMatrix = distanceMatrix
        else:
            self.__NodeList = np.array([], dtype = type(nd.Node))
            self.__coordinateMode = True

####### Check if given distance matrix is a valid distance Matrix. Depending on 
####### errorMode, choose to either raise an error or return false. 
    def checkDistanceMatrix(self, distanceMatrix, errorMode = True):
        """
        Checks whether the given distance matrix is a `valid`_ distance matrix
        
        Parameters
        ----------
        
            distanceMatrix: numpy.array
            errorMode: boolean, optional
        
        If errorMode is set to True, then errors will be raised, ending code execution
        Otherwise, the function will return False
        
        .. _valid: https://cspath.readthedocs.io/en/latest/how-to/graph-parse.html
        
        """
        if not isinstance(distanceMatrix[0], np.ndarray):
            if errorMode:
                raise ValueError(f"Expected {np.ndarray} and got {type(distanceMatrix[0])}.")
            else:
                return False

        if not isinstance(distanceMatrix[0][0], (np.float64, np.float32, np.int64, np.int32, np.int16, np.int8)):
            if errorMode:
                raise ValueError(f"Expected {np.float64} or {np.int64} for matrix entries and got {type(distanceMatrix[0][0])}.")
            else:
                return False

        matrix_num = len(distanceMatrix) 
        
        for i in np.arange(matrix_num):

            for j in np.arange(i, matrix_num):

                if i != j:

                    if distanceMatrix[i][j] * distanceMatrix[j][i] == 0:
                        if errorMode:
                            raise ValueError(f"Zero entry not on main diagonal: ({i, j}, {j, i}) = ({distanceMatrix[i][j]}, {distanceMatrix[j][i]}).")
                        else:
                            return False

                else:

                    if distanceMatrix[i][i] != 0:
                        if errorMode:
                            raise ValueError(f"'Main' diagonal entry {i, i} is {distanceMatrix[i][i]} (not 0).")
                        else:
                            return False

        return True

######################################
#       GETTERS AND SETTERS          #
######################################

    def getCoordinateMode(self):
        """
        Returns :code:`True` if coordinates are used for graph parsing. :code:`False`, otherwise.
        """
        return self.__coordinateMode
    
    def get3DMode(self):
        """
        If coordinates are used for graph parsing, return true if the graph is 3-dimensional. False if not.
        Otherwise, return None
        """
        if self.__coordinateMode:
            return self.__3D
        return None

####### Distance Matrix getter, setter and checker.
    def IsValidDistanceMatrix(self, distanceMatrix, errorMode = False):
        """
        Essentially the same with checkDistanceMatrix, only errorMode = False by default
        """
        return self.checkDistanceMatrix(distanceMatrix, errorMode)
    
    def setDistanceMatrix(self, distanceMatrix, errorMode = False):
        """
        Uses checkDistanceMatrix to see if the given distanceMatrix is valid. If so, it sets the 
        current distanceMatrix to the given. Otherwise returns False
        
        Parameters
        ----------
        
            distanceMatrix: numpy.array
            errorMode: boolean, optional
        
        """
        if self.checkDistanceMatrix(distanceMatrix, errorMode):
            self.__distMatrix = distanceMatrix
            return True
        else:
            return False

    def getDistanceMatrix(self):
        """
        Returns current distanceMatrix
        
        Returns
        -------
        
            distanceMatrix: numpy.array
        """
        return self.__distMatrix

####### Add a node to the Node list. Update distance matrix.
    def addNode(self, x, y, z):
        """
        If we are in coordinate mode, checks if the node with given coordinates is in nodeList. If not, it adds it.
        Otherwise, returns False
        
        Parameters
        ----------
        
            x: float or int
            y: float or int
            z: float or int
        
        Returns
        -------
        
            curr: cspath.Node
  
        """
        if self.__coordinateMode:

            nx = np.float64(x)
            ny = np.float64(y)
            nz = np.float64(z)

            if nz != 0 and not self.__3D:
                self.__3D = True

            curr = nd.Node(nx, ny, nz)

            if not nd.nodeInList(curr, self.__NodeList):
                self.__NodeList = np.append(self.__NodeList, curr)
                
                if len(self.__distMatrix) == 0:
                    self.__distMatrix = np.append(self.__distMatrix, np.array(0))
                    self.__distMatrix = np.resize(self.__distMatrix, (1, 1))
                else:
                    temp = np.resize(-np.inf, (len(self.__NodeList), len(self.__NodeList)))
                    temp[len(self.__NodeList) - 1][len(self.__NodeList) - 1] = 0
                    for i in np.arange(len(self.__distMatrix)):
                        for j in np.arange(len(self.__distMatrix)):
                            temp[i][j] = self.__distMatrix[i][j]
                    self.__distMatrix = temp

                return curr
            else:
                return None
    
####### Change the coordinates of an existing node.
    def changeNode(self, i, x, y, z):
        """
        Changes node i's coordinates to x, y, z after checking no node with x, y, z coordinates exists in the nodeList
        
        Parameters
        ----------
        
            i: int, index of Node in the list
            x: float or int
            y: float or int
            z: float or int
        """
        if self.__coordinateMode:

            ni = np.uint64(i)
            nx = np.float64(x)
            ny = np.float64(y)
            nz = np.float64(z)

            if ni < len(self.__NodeList):
                if not nd.nodeInList(nd.Node(nx, ny, nz), self.__NodeList):
                    self.__NodeList[ni].setNode(nx, ny, nz)

                    for i in np.arange(len(self.__distMatrix)):
                        t = np.linalg.norm(self.__NodeList[ni].get() - self.__NodeList[i].get())
                        if self.__distMatrix[ni][i] > 0:
                            self.__distMatrix[ni][i] = t 
                        if self.__distMatrix[i][ni] > 0:
                            self.__distMatrix[ni][i] = t

####### Return the list of current nodes.
    def getNodeList(self):
        """
        Returns the nodeList
        
        Returns
        -------
            
            cspath.Graph.__NodeList: numpy.array of cspath.Node types
        
        """
        return self.__NodeList

######################################
#        LINKING NODES               #
######################################

####### Create a link between two specified nodes.
    def linkNodes(self, i, j, sdirect):
        """
        Adds an edge between two nodes. If sdirect is set to True, it is undirected. Otherwise, it is directed from 
        node i to node j. The weight of the edge is the euclidean distance between the two nodes
        
        Parameters
        ----------
        
            i: int
            j: int
            sdirect: boolean
        """
        ni = np.uint64(i)
        nj = np.uint64(j)

        if ni != nj and ni < len(self.__NodeList) and nj < len(self.__NodeList) and isinstance(sdirect, bool):
            dist = np.linalg.norm(self.__NodeList[ni].get() - self.__NodeList[nj].get())

            self.__distMatrix[ni][nj] = dist
            if sdirect:
                self.__distMatrix[nj][ni] = dist
    
####### Delete a link between two specified nodes.
    def delLink(self, i, j, sdirect):
        """
        Removes an edge between two nodes. If sdirect is set to True, the edge is removed completely. If False and the edge
        is undirected, what remains is only a directed edge from node i to node j.
        
        Parameters
        ----------
            i: int
            j: int
            sdirect: boolean
        
        """
        ni = np.uint64(i)
        nj = np.uint64(j)

        if ni != nj and ni < len(self.__NodeList) and nj < len(self.__NodeList) and isinstance(sdirect, bool):

            self.__distMatrix[ni][nj] = -np.inf
            if sdirect:
                self.__distMatrix[nj][ni] = -np.inf
        
######################################
#       ALGORITHM IMPLEMENTATION     #
######################################

####### Dijkstra's Algorithm Implementation Version 1 (Without using heaps).
    def dijkstra(self):
        """
        Standard implementation of Dijkstra's algorithm. More information can be found `here`_.
        
        Returns
        -------
            tour: numpy.array containing shortest path
            shrDist: float or int, length of tour
            duration: float or int, algorithm runtime in seconds
        
        .. _here: https://cspath.readthedocs.io/en/latest/explanation/index.html
        """
        start = time()

        numNodes = len(self.__distMatrix)

        if numNodes == 0:
            return None, None, None

        shr = np.array([],  dtype = np.float64)

        prev = np.array([], dtype = np.uint64)
        
        vis  = np.array([], dtype = np.bool)

        for i in np.arange( numNodes):

            if self.__distMatrix[0][i] >= 0:
                prev = np.insert(prev, i, 0)
                shr  = np.insert(shr, i, self.__distMatrix[0][i])
            else:
                prev = np.insert(prev, i,  -1)
                shr  = np.insert(shr, i, np.inf)

            vis = np.insert(vis, i, False)
        
        vis[0] = True
        numTrue = 1

        while numTrue < numNodes:

            min_idx = 1 

            for j in np.arange(1, numNodes):

                if not vis[j]:
                    min_idx = j
                    break
            
            for i in np.arange(numNodes):
                
                if shr[i] < shr[min_idx] and not vis[i]:
                    min_idx = i
            
            for h in np.arange(numNodes):

                if vis[h]:
                    continue

                if self.__distMatrix[min_idx][h] > 0 and self.__distMatrix[min_idx][h] + shr[min_idx] < shr[h]:
                    shr[h] = self.__distMatrix[min_idx][h] + shr[min_idx]
                    prev[h] = min_idx
        
            
            if min_idx == numNodes - 1:
                break

            vis[min_idx] = True
            numTrue += 1

        end = time()

        if shr[numNodes - 1] == np.inf:
            return None, None, end - start

        tour = np.array([numNodes - 1], dtype = np.uint64)
        g = prev[numNodes - 1]

        while g:

            tour = np.append(tour, g)
            g = prev[g]

        tour = np.append(tour, 0)
        tour = np.flip(tour)

        return tour, shr[numNodes - 1], end - start

####### Dijkstra's Algorithm Implementation Version 2 (Making use of an indexed priority queue).
    def ipq_dijkstra(self):
        """
        Indexed Priority Queue implementation of Dijkstra's algorithm. More information can be found `here`_.
        
        Returns
        -------
            tour: numpy.array containing shortest path
            shrDist: float or int, length of tour
            duration: float or int, algorithm runtime in seconds
        
        .. _here: https://cspath.readthedocs.io/en/latest/explanation/index.html
        """
        try:
            from pqdict import pqdict

            start = time()

            numNodes = len(self.__distMatrix)

            if numNodes == 0:
                return None, None, None

            vis = np.array([], dtype = np.bool)
            shr = np.array([], dtype = np.float64)
            prev = np.array([], dtype = np.int64)
            ipq = pqdict({0 : 0})

            for i in np.arange(numNodes):
                vis = np.insert(vis, i, False)
                shr = np.insert(shr, i, np.inf)
                prev = np.insert(prev, i, -1)

            shr[0] = 0

            while len(ipq):

                index, minValue = ipq.popitem()
                vis[index] = True

                if shr[index] < minValue:
                    continue
                
                for i in np.arange(numNodes):
                    
                    if vis[i]:
                        continue

                    if self.__distMatrix[index][i] > 0 and self.__distMatrix[index][i] + shr[index] < shr[i]:
                        shr[i] = self.__distMatrix[index][i] + shr[index]
                        prev[i] = index

                        ##### This is a very ugly hack, lol. 
                        try:
                            ipq.additem(i, shr[i])
                        except KeyError:
                            ipq.updateitem(i, shr[i])
                
                if index == numNodes - 1:
                    break

            end = time()

            if shr[numNodes - 1] == np.inf:
                return None, None, end - start

            tour = np.array([numNodes - 1], dtype = np.uint64)
            g = prev[numNodes - 1]

            while g:

                tour = np.append(tour, g)
                g = prev[g]

            tour = np.append(tour, 0)
            tour = np.flip(tour)

            return tour, shr[numNodes - 1], end - start

        except ImportError:
            print("Please install module 'pqdict' for this function to work. ^_^")
            print("More information on 'pqdict' can be found here https://pypi.org/project/pqdict/.")

####### Dijkstra's Algorithm Implementation Version 3 (Returns shortest distances from start node to all other nodes and previous vertices without heaps).

    def dijkstra_all(self):
        """
        Standard implementation of Dijkstra's algorithm with extra outputs. More information can be found `here`_.
        
        Returns
        -------
            shr: numpy.array containing shortest distances to all nodes from start node
            tour: numpy.array containing shortest path
            prev: numpy.array containing previously visited nodes
            shrDist: float or int, length of tour
            duration: float or int, algorithm runtime in seconds
        
        
        .. _here: https://cspath.readthedocs.io/en/latest/explanation/index.html
        """        
        start = time()

        numNodes = len(self.__distMatrix)

        if numNodes == 0:
            return None, None, None, None, None

        shr = np.array([],  dtype = np.float64)

        prev = np.array([], dtype = np.uint64)
        
        vis  = np.array([], dtype = np.bool)

        for i in np.arange( numNodes):

            if self.__distMatrix[0][i] >= 0:
                prev = np.insert(prev, i, 0)
                shr  = np.insert(shr, i, self.__distMatrix[0][i])
            else:
                prev = np.insert(prev, i,  -1)
                shr  = np.insert(shr, i, np.inf)

            vis = np.insert(vis, i, False)
        
        vis[0] = True
        numTrue = 1

        while numTrue < numNodes:

            min_idx = 1 

            for j in np.arange(1, numNodes):

                if not vis[j]:
                    min_idx = j
                    break
            
            for i in np.arange(numNodes):
                
                if shr[i] < shr[min_idx] and not vis[i]:
                    min_idx = i
            
            for h in np.arange(numNodes):

                if vis[h]:
                    continue

                if self.__distMatrix[min_idx][h] > 0 and self.__distMatrix[min_idx][h] + shr[min_idx] < shr[h]:
                    shr[h] = self.__distMatrix[min_idx][h] + shr[min_idx]
                    prev[h] = min_idx
        
            
            if min_idx == numNodes - 1:
                break

            vis[min_idx] = True
            numTrue += 1

        end = time()

        if shr[numNodes - 1] == np.inf:
            return shr, prev, None, None, end - start

        tour = np.array([numNodes - 1], dtype = np.uint64)
        g = prev[numNodes - 1]

        while g:

            tour = np.append(tour, g)
            g = prev[g]

        tour = np.append(tour, 0)
        tour = np.flip(tour)

        return shr, prev, tour, shr[numNodes - 1], end - start

####### Dijkstra's Algorithm Implementation Version 4 (Returns shortest distances from start node to all other nodes and previous vertices using an indexed priority queue).
    def ipq_dijkstra_all(self):
        """
        Indexed Priority Queue implementation of Dijkstra's algorithm with extra outputs. More information can be found `here`_.
        
        Returns
        -------
            shr: numpy.array containing shortest distances to all nodes from start node
            tour: numpy.array containing shortest path
            prev: numpy.array containing previously visited nodes
            shrDist: float or int, length of tour
            duration: float or int, algorithm runtime in seconds
        
        
        .. _here: https://cspath.readthedocs.io/en/latest/explanation/index.html
        """       

        try:
            from pqdict import pqdict

            start = time()

            numNodes = len(self.__distMatrix)

            if numNodes == 0:
                return None, None, None, None, None

            vis = np.array([], dtype = np.bool)
            shr = np.array([], dtype = np.float64)
            prev = np.array([], dtype = np.int64)
            ipq = pqdict({0 : 0})

            for i in np.arange(numNodes):
                vis = np.insert(vis, i, False)
                shr = np.insert(shr, i, np.inf)
                prev = np.insert(prev, i, -1)

            shr[0] = 0

            while len(ipq):

                index, minValue = ipq.popitem()
                vis[index] = True

                if shr[index] < minValue:
                    continue
                
                for i in np.arange(numNodes):
                    
                    if vis[i]:
                        continue

                    if self.__distMatrix[index][i] > 0 and self.__distMatrix[index][i] + shr[index] < shr[i]:
                        shr[i] = self.__distMatrix[index][i] + shr[index]
                        prev[i] = index

                        ##### This is a very ugly hack, lol. 
                        try:
                            ipq.additem(i, shr[i])
                        except KeyError:
                            ipq.updateitem(i, shr[i])
                
                if index == numNodes - 1:
                    break

            end = time()

            if shr[numNodes - 1] == np.inf:
                return shr, prev, None, None, end - start

            tour = np.array([numNodes - 1], dtype = np.uint64)
            g = prev[numNodes - 1]

            while g:

                tour = np.append(tour, g)
                g = prev[g]

            tour = np.append(tour, 0)
            tour = np.flip(tour)

            return shr, prev, tour, shr[numNodes - 1], end - start

        except ImportError:
            print("Please install module 'pqdict' for this function to work. ^_^")
            print("More information on 'pqdict' can be found here https://pypi.org/project/pqdict/.")

####### A* Algorithm Implementation.
    def a_star(self):
        """
        Standard implementation of A* Algorithm. More information can be found `here`_.
        
        Returns
        -------
            tour: numpy.array containing shortest path
            shrDist: float or int, length of tour
            duration: float or int, algorithm runtime in seconds
        
        .. _here: https://cspath.readthedocs.io/en/latest/explanation/index.html
        """
        if not self.__coordinateMode:
            return self.dijkstra()
        

        ###### The chosen heuristic is the euclidean distance. 
        ###### This makes a lot of sense since we are dealing
        ###### with cartesian coordinates.
        start = time()

        numNodes = len(self.__distMatrix)

        if numNodes == 0:
            return None, None, None

        vis = np.array([], dtype = np.bool)

        prev = np.array([], dtype = np.int64)

        heur = np.array([], dtype = np.float64)

        shrDist = np.array([], dtype = np.float64)

        for i in np.arange(numNodes):
            vis = np.append(vis, False)
            heur = np.append(heur, np.linalg.norm(self.__NodeList[0].get() - self.__NodeList[i].get()))
            if self.__distMatrix[0][i] >= 0:
                prev = np.insert(prev, i, 0)
                shrDist  = np.insert(shrDist, i, self.__distMatrix[0][i])
            else:
                prev = np.insert(prev, i,  -1)
                shrDist  = np.insert(shrDist, i, np.inf)
        
        vis[0] = True
        numVis = 1

        while numVis < len(vis):

            min_idx = 1

            for i in np.arange(1, numNodes):

                if not vis[i]:
                    min_idx = i
                    break

            for j in np.arange(1, numNodes):

                if heur[j] + shrDist[j] < heur[min_idx] + shrDist[min_idx] and not vis[j]:
                    min_idx = j

            for h in np.arange(numNodes):
                if self.__distMatrix[min_idx][h] > 0 and shrDist[min_idx] + self.__distMatrix[min_idx][h] < shrDist[h]:
                    shrDist[h] = shrDist[min_idx] + self.__distMatrix[min_idx][h]
                    prev[h] = min_idx

            if min_idx == numNodes - 1:
                break

            vis[min_idx] = True
            numVis += 1

        end = time()

        if shrDist[numNodes - 1] == np.inf:
            return None, None, end - start

        tour = np.array([numNodes - 1], dtype = np.uint64)
        g = prev[numNodes - 1]

        while g:

            tour = np.append(tour, g)
            g = prev[g]

        tour = np.append(tour, 0)
        tour = np.flip(tour)

        return tour, shrDist[numNodes - 1], end - start

####### Bellman-Ford Algorithm Implementation.
    def bellman_ford(self):
        """
        Standard implementation of Bellman-Ford algorithm. More information can be found `here`_.
        
        Returns
        -------
            tour: numpy.array containing shortest path
            shrDist: float or int, length of tour
            duration: float or int, algorithm runtime in seconds
        
        .. _here: https://cspath.readthedocs.io/en/latest/explanation/index.html
        """
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

        for i in np.arange(1, numNodes):
            
            for a in np.arange(numNodes):
                for b in np.arange(numNodes):

                    if a != b and self.__distMatrix[a][b] != -np.inf:
                        if self.__distMatrix[a][b] + shr[a] <  shr[b]:
                            shr[b] = self.__distMatrix[a][b] + shr[a]
                            prev[b] = a
        end = time()

        for a in np.arange(numNodes):
            for b in np.arange(numNodes):

                if a != b and self.__distMatrix[a][b] + shr[a] < shr[b] and self.__distMatrix[a][b] != -np.inf:
                    return None, "Detected Negative Cycle", end - start

        if shr[numNodes - 1] == np.inf:
            return None, None, end - start

        tour = np.array([numNodes - 1], dtype = np.uint64)
        g = prev[numNodes - 1]

        while g:

            tour = np.append(tour, g)
            g = prev[g]

        tour = np.append(tour, 0)
        tour = np.flip(tour)

        return tour, shr[numNodes - 1], end - start

    def bellman_ford_all(self):
        """
        Standard implementation of Bellman-Ford with extra outputs. More information can be found `here`_.
        
        Returns
        -------
            shr: numpy.array containing shortest distances to all nodes from start node
            tour: numpy.array containing shortest path
            prev: numpy.array containing previously visited nodes
            shrDist: float or int, length of tour
            duration: float or int, algorithm runtime in seconds
        
        
        .. _here: https://cspath.readthedocs.io/en/latest/explanation/index.html
        """   
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

        for i in np.arange(1, numNodes):
            
            for a in np.arange(numNodes):
                for b in np.arange(numNodes):

                    if a != b and self.__distMatrix[a][b] != -np.inf:
                        if self.__distMatrix[a][b] + shr[a] <  shr[b]:
                            shr[b] = self.__distMatrix[a][b] + shr[a]
                            prev[b] = a
        end = time()

        for a in np.arange(numNodes):
            for b in np.arange(numNodes):

                if a != b and self.__distMatrix[a][b] + shr[a] < shr[b] and self.__distMatrix[a][b] != -np.inf:
                    return "Detected Negative Cycle", None, None, None,  end - start

        if shr[numNodes - 1] == np.inf:
            return None, None, None, None, end - start

        tour = np.array([numNodes - 1], dtype = np.uint64)
        g = prev[numNodes - 1]

        while g:

            tour = np.append(tour, g)
            g = prev[g]

        tour = np.append(tour, 0)
        tour = np.flip(tour)

        return shr, prev, tour, shr[numNodes - 1], end - start

####### Floyd-Warshall Algorithm Implementation.
    def floyd_warshall(self):
        """
        Standard implementation of Floyd-Warshall. More information can be found `here`_.
        
        Returns
        -------
            tour: numpy.array containing shortest path
            shrDist: float or int, length of tour
            duration: float or int, algorithm runtime in seconds
        
        
        .. _here: https://cspath.readthedocs.io/en/latest/explanation/index.html
        """   
        numNodes = len(self.__distMatrix)

        if numNodes == 0:
            return None, None, None, None, None

        start = time()

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

        for k in np.arange(numNodes):
            for i in np.arange(numNodes):
                for j in np.arange(numNodes):
                    if M[i][j] > M[i][k] + M[k][j]:
                        M[i][j] = M[i][k] + M[k][j]
                        prev[i][j] = prev[i][k] 
        end = time()

        if M[numNodes-1][numNodes-1] == np.inf:
            return None, None, end-start
        
        tour = np.array([], dtype = np.uint64)

        u = 0

        tour = np.append(tour, u)

        while u != numNodes - 1:
            u = prev[u][numNodes - 1]
            tour = np.append(tour, u)


        return tour, M[0][numNodes - 1], end - start

######################################
#  GENERAL GRAPH ANALYSIS UTILITIES  #
######################################

####### Get Out Degree of Node. If negIntr is set to True, we consider
####### negative values of the distance matrix as neighbors with negative weight.
    def get_odegree(self, node, negIntr = False):
        deg = 0
        for i in np.arange(len(self.__distMatrix)):
            if self.__distMatrix[node][i] > 0:
                deg += 1
            if negIntr:
                if self.__distMatrix[node][i] < 0 and self.__distMatrix[node][i] != -np.inf:
                    deg += 1
        return deg

####### Get In Degree of Node. If negIntr is set to True, we consider
####### negative values of the distance matrix as neighbors with negative weight.
    def get_idegree(self, node, negIntr = False):

        deg = 0
        for i in np.arange(len(self.__distMatrix)):
            if self.__distMatrix[i][node] > 0:
                deg += 1
            if negIntr:
                if self.__distMatrix[i][node] < 0 and self.__distMatrix[i][node] != -np.inf:
                    deg += 1
        return deg

####### Get In Neighbors of Node. If negIntr is set to True, we consider
####### negative values of the distance matrix as neighbors with negative weight.
    def get_oneighbors(self, node, negIntr = False):
        
        oneighs = np.array([], dtype = np.uint64)

        for i in np.arange(len(self.__distMatrix)):
            if self.__distMatrix[node][i] > 0:
                oneighs  = np.append(oneighs, i)
            if negIntr:
                if self.__distMatrix[node][i] < 0 and self.__distMatrix[node][i] != -np.inf:
                    oneighs = np.append(oneighs, i)
        return oneighs

    
####### Get Out Neighbors of Node. If negIntr is set to True, we consider
####### negative values of the distance matrix as neighbors with negative weight.
    def get_ineighbors(self, node, negIntr = False):

        oneighs = np.array([], dtype = np.uint64)

        for i in np.arange(len(self.__distMatrix)):
            if self.__distMatrix[i][node] > 0:
                oneighs  = np.append(oneighs, i)
            if negIntr:
                if self.__distMatrix[i][node] < 0 and self.__distMatrix[i][node] != -np.inf:
                    oneighs = np.append(oneighs, i)
        return oneighs
