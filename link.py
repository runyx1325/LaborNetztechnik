class linkClass:
    def __init__(self, node1, node2, linkWeight):
        self.node1 = node1
        self.node2 = node2
        self.weight = linkWeight

    def __str__(self):
        return self.node1 + "-" + self.node2

    @property
    def get_weight(self):
        return self.weight

    @property
    def get_node1(self):
        return self.node1

    @property
    def get_node2(self):
        return self.node2
