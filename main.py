import re
from settings import settingsClass
from helper import *
from node import nodeClass
from link import linkClass

if __name__ == '__main__':
    settings = settingsClass()
    itemCounter = 0
    with open(settings.inputFile, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("//") or line.startswith("#"):
                continue
            itemCounter += 1
    # check if number of lines in inputFile is smaller then MAX_ITEMS
    if itemCounter <= settings.MAX_ITEMS:
        #first read: all nodes
        nodeDict = {}
        with open(settings.inputFile, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("//") or line.startswith("#"):
                    continue
                elif re.match(settings.nodePattern, line):
                    nodeName = re.match(settings.nodePattern, line).group(1)
                    nodeID = int(re.match(settings.nodePattern, line).group(2))
                    if validateNodeData(nodeName, nodeID, nodeDict, settings):
                        #create Node
                        nodeDict[nodeName] = nodeClass(nodeName, nodeID)


        #second read: all links
        with open(settings.inputFile, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("//") or line.startswith("#"):
                    continue
                if re.match(settings.linkPattern, line):
                    linkNode1 = re.match(settings.linkPattern, line).group(1)
                    linkNode2 = re.match(settings.linkPattern, line).group(2)
                    linkWeight = int(re.match(settings.linkPattern, line).group(3))
                    if validateLinkData(linkNode1, linkNode2, linkWeight, nodeDict, settings):
                        #get node objects
                        node1 = nodeDict[linkNode1]
                        node2 = nodeDict[linkNode2]
                        #create Link
                        node1.link(node2.get_name, linkWeight)
                        node2.link(node1.get_name, linkWeight)

        print("All Nodes:")
        for x in nodeDict.values():
            print(x)

        print("All Links:")
        for x in nodeDict.values():
            for y in x.get_linkDict.values():
                print(y)

