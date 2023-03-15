#Hier kommen Konstanten und anderer Hardcode hin
class settingsClass():
    def __init__(self):
        self.inputFile = "input.txt"
        # Node: Aaaa = 10101001;
        self.nodePattern = r'^([a-zA-Z][a-zA-Z0-9]{0,3}) = (\d+);$'
        # Link: Aaaa - Bbbb = 1010021010;
        self.linkPattern = r'^([a-zA-Z][a-zA-Z0-9]{0,3}) - ([a-zA-Z][a-zA-Z0-9]{0,3}) : (\d+);$'
        self.MAX_IDENT = 3              #max length of node name
        self.MAX_ITEMS = 10             #max lines in inputfile
        self.MAX_KOSTEN = 50            #0 - max costs for edge
        self.MAX_NODE_ID = 10000        #1 - max node id


        self._SettingsDict = {
            'inputFile': "input.txt",
            'MAX_IDENT': 3,
            'MAX_ITEMS': 10,
            'MAX_KOSTEN': 50,
            'MAX_NODE_ID': 10000
        }