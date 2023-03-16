from link import linkClass
class nodeClass():
    def __init__(self, nodeName, nodeID):
        self.nodeName = nodeName
        self.nodeID = nodeID
        self.nextNode = self
        self.rootNode = self
        self.wayToRoot = 0
        self.count = 0
        self.linkDict = {}

    def __str__(self):
        return self.nodeName
    @property
    def get_ID(self):
        return self.nodeID
    @property
    def get_name(self):
        return self.nodeName
    @property
    def get_nextNode(self):
        return self.nextNode
    @property
    def get_rootNode(self):
        return self.rootNode
    @property
    def get_rootWay(self):
        return self.wayToRoot
    @property
    def get_linkDict(self):
        return self.linkDict
    @property
    def get_count(self):
        return self.count
    def link(self, node, weight):
        if node is not self.linkDict:
            self.linkDict[node] = linkClass(self.get_name, node, weight)

    def count(self):
        self.count += 1

    def send(self, nodeDict):
        for link in self.get_linkDict.values():
            #send to all neighbours rootNode, rootWayWeight and node
            #Ich (self) kenne einen Weg zu Root mit der ID (rootNode.get_ID) und den Kosten (self.get_rootWay)
            nodeDict.get(link.get_node2).recive(self.get_rootNode, self.get_rootWay, self)

    def recive(self, rootNode, rootWayWeight, node):
        #Wenn der übergebene Rootknoten eine kleinere ID hat als der bisherige
        if rootNode.get_ID < self.get_rootNode.get_ID:
                self.rootNode = rootNode
                self.nextNode = node
                self.wayToRoot = rootWayWeight + self.get_linkDict.get(node.get_name).get_weight
        elif rootNode.get_ID == self.get_rootNode.get_ID:
            if rootWayWeight + self.get_linkDict.get(node.get_name).get_weight < self.wayToRoot:
                self.nextNode = node
                self.wayToRoot = rootWayWeight + self.get_linkDict.get(node.get_name).get_weight