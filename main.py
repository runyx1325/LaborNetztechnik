import re
from settings import settingsClass
from helper import *

if __name__ == '__main__':
    settings = settingsClass()
    #Node: Aaaa = 10101001;
    nodePattern = r'^([a-zA-Z][a-zA-Z0-9]{0,3}) = (\d+);$'
    #Link: Aaaa - Bbbb = 1010021010;
    linkPattern = r'^([a-zA-Z][a-zA-Z0-9]{0,3}) - ([a-zA-Z][a-zA-Z0-9]{0,3}) : (\d+);$'
    #first read: all nodes
    with open(settings._SettingsDict['inputFile'], "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("//") or line.startswith("#"):
                continue
            elif re.match(nodePattern, line):
                nodeName = re.match(nodePattern, line).group(1)
                nodeID = re.match(nodePattern, line).group(2)
                if validateNodeData(nodeName, nodeID):
                    #create Node
                    pass

    #second read: all links
    with open(settings._SettingsDict['inputFile'], "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("//") or line.startswith("#"):
                continue
            if re.match(linkPattern, line):
                linkNode1 = re.match(linkPattern, line).group(1)
                linkNode2 = re.match(linkPattern, line).group(2)
                linkWeight = re.match(linkPattern, line).group(3)
                if validateLinkData(linkNode1, linkNode2, linkWeight):
                    #create Link
                    pass

