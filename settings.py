#Hier kommen Konstanten und anderer Hardcode hin
class settingsClass():
    def __init__(self):
        self.inputFile = "input.txt"
        self.MAX_IDENT = 3              #max length of node name
        self.MAX_ITEMS = 30             #max lines in inputfile
        self.MAX_KOSTEN = 50            #0 - max costs for edge
        self.MAX_NODE_ID = 10000        #1 - max node id
        # Node: Aaaa = 10101001;
        self.nodePattern = r'^([a-zA-Z][a-zA-Z0-9]{0,' + str(self.MAX_IDENT) + r'}) = (\d+);$'
        # Link: Aaaa - Bbbb = 1010021010;
        self.linkPattern = r'^([a-zA-Z][a-zA-Z0-9]{0,' + str(self.MAX_IDENT) + r'}) - ([a-zA-Z][a-zA-Z0-9]{0,' + str(self.MAX_IDENT) + r'}) : (\d+);$'
        self.countBPDU = 0