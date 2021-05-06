"""A class for handling Nodes described by 3D Cartesian Coordinates"""
import numpy as np
###############################
#           NODE CLASS        #
###############################

class Node:
    """
    A class for handling Nodes described by 3D Cartesian Coordinates
    Initializes instance of :code:`cspath.Node` with coordinates x, y, z
        
    Parameters
    ----------
        
        x: float or int
        y: float or int
        z: float or int
    """
    def __init__(self, x, y, z):
        self.__vec = np.array([np.float64(x), np.float64(y), np.float64(z)])

    def get(self):
        """
        Get coordinates of Node as :code:`numpy.array`
        
        Returns
        -------
        
            cspath.Node.__vec: numpy.array
        """
        return self.__vec
    
    def setX(self, x):
        """
        Set x-coordinate of Node
        
        Parameters
        ----------
        
            x: float or int
        """
        nx = np.float64(x)
        self.__vec[0] = nx

    def setY(self, y):
        """
        Set y-coordinate of Node
        
        Parameters
        ----------
        
            y: float or int
        """
        ny = np.float64(y)
        self.__vec[1] = ny
    
    def setZ(self, z):
        """
        Set z-coordinate of Node
        
        Parameters
        ----------
        
            z: float or int
        """
        nz = np.float64(z)
        self.__vec[2] = nz

    def setNode(self, x, y, z):
        """
        Set x,y,z coordinates of Node
        
        Parameters
        ----------
        
            x: float or int
            y: float or int
            z: float or int
        """
        self.setX(x)
        self.setY(y)
        self.setZ(z)

    def __repr__(self):
        return f"Node @ ({self.__vec[0]}, {self.__vec[1]}, {self.__vec[2]})"

################################
#           HELPERS            #
################################

def nodeEq(Node1, Node2):
    """
    Check if two instances of the Node class have the same coordinates
    
    Parameters
    ----------
    
        Node1: cspath.Node
        Node2: cspath.Node
    
    Returns True if yes, False otherwise.
    """
    a = Node1.get()
    b = Node2.get()

    if a[0] != b[0] or a[1] != b[1] or a[2] != b[2]:
        return False
    return True

def nodeInList(Node1, nodeList):
    """
    Check if one instance of the Node class is in a nodeList
    
    Parameters
    ----------
    
        Node1: cspath.Node
        nodeList: numpy.array of cspath.Node instances
     
    Returns True if yes, False otherwise.
    """
    for i in np.arange(len(nodeList)):

        if nodeEq(nodeList[i], Node1):
            return True

    return False
