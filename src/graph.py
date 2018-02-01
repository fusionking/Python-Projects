################# CAN ARSOY 18076 ######################

class Node:
    def __init__(self,key,posX,posY,posX2,posY2,path_cost=0,reachable=True):

        # self.key is the key of node (unique)
        # self.successors are the successors nodes
        # self.weight_successors represents weight of edges
        # self.posX,self.posY represents the position of the block
        self.key = key
        self.posX = posX
        self.posY = posY
        self.posX2 = posX2
        self.posY2 = posY2
        self.path_cost = path_cost
        self.reachable = reachable
        self.successors = []

    # return the key
    def getKey(self):
        return self.key

    def getPos(self):
        return self.posX,self.posY,self.posX2,self.posY2


    # add a node successor passing the node and the weight
    def addSuccessor(self, node):
            self.successors.append(node)


    def updateNode(self,distance):
        self.path_cost = distance

    def find(self, t):
        """Return the node for key t if it is in this tree, or None otherwise."""
        if t == self.key:
            return self

    def expand(self):
        "List the nodes reachable in one step from this node"

        return self.successors


########################################################################################################################
########################################################################################################################

# class that represents a graph
class Graph:
    def __init__(self):
        self.nodes = {}  # key: key of node, value: instance of Node


    def addNode(self,key_node,posX,posY,posX2,posY2,path_cost,reachable):

            node = Node(key_node,posX,posY,posX2,posY2,path_cost,reachable)  # creates a instance of Node
            self.nodes[key_node,posX,posY,posX2,posY2,path_cost,reachable] = node  # stores the node

    # connects the nodes
    def connect(self, key_source, key_source_posX,key_source_posY,key_source_posX2,key_source_posY2,key_destination,key_destination_posX,key_destination_posY,
                key_destination_posX2,key_destination_posY2):
                    # connects the nodes
                    self.nodes[key_source,key_source_posX,key_source_posY,key_source_posX2,key_source_posY2,0,True].addSuccessor(
                        self.nodes[key_destination,key_destination_posX,key_destination_posY,key_destination_posX2,key_destination_posY2,0,True])

    def getKeys(self):
        return self.nodes.keys()

    # returns all nodes
    def getNodes(self):
        return self.nodes

    def updateGraph(self,graph,key,posX,posY,posX2,posY2,path_cost,reachable,distance):
        graph.nodes[key, posX, posY, posX2, posY2, path_cost, reachable].path_cost = distance










