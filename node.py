from link import linkClass
class nodeClass():
    def __init__(self, nodeName, nodeID):
        self.nodeName = nodeName
        self.nodeID = nodeID
        self.wayToRoot = 0
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
    def get_rootWay(self):
        return self.wayToRoot
    @property
    def get_linkDict(self):
        return self.linkDict

    def link(self, node, weight):
        if node is not self.linkDict:
            self.linkDict[node] = linkClass(self.get_name, node, weight)

