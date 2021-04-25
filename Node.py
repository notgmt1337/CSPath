import numpy as np

###############################
#           NODE CLASS        #
###############################

class Node:
    
    def __init__(self, x, y, z):

        self.__vec = np.array([np.float64(x), np.float64(y), np.float64(z)])

    def get(self):

        return self.__vec
    
    def setX(self, x):
        nx = np.float64(x)
        self.__vec[0] = nx

    def setY(self, y):
        ny = np.float64(y)
        self.__vec[1] = ny
    
    def setZ(self, z):
        nz = np.float64(z)
        self.__vec[2] = nz

    def setNode(self, x, y, z):
        self.setX(x)
        self.setY(y)
        self.setZ(z)

    def __repr__(self):
        return f"Node @ ({self.__vec[0]}, {self.__vec[1]}, {self.__vec[2]})"

################################
#           HELPERS            #
################################

def nodeEq(Node1, Node2):

    a = Node1.get()
    b = Node2.get()

    if a[0] != b[0] or a[1] != b[1] or a[2] != b[2]:
        return False
    return True

def nodeInList(Node1, nodeList):

    for i in np.arange(len(nodeList)):

        if nodeEq(nodeList[i], Node1):
            return True

    return False