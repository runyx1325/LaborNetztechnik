import re
from settings import settingsClass
from helper import *
from node import nodeClass
from link import linkClass

if __name__ == '__main__':
    settings = settingsClass()
    #first read: all nodes
    nodeDict = {}
    with open(settings.inputfile, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("//") or line.startswith("#"):
                continue
            elif re.match(settings.nodePattern, line):
                nodeName = re.match(settings.nodePattern, line).group(1)
                nodeID = re.match(settings.nodePattern, line).group(2)
                if validateNodeData(nodeName, nodeID, nodeDict, settings):
                    #create Node
                    nodeDict[nodeName] = nodeClass(nodeName, nodeID)


    #second read: all links
    with open(settings.inputfile, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("//") or line.startswith("#"):
                continue
            if re.match(settings.linkPattern, line):
                linkNode1 = re.match(settings.linkPattern, line).group(1)
                linkNode2 = re.match(settings.linkPattern, line).group(2)
                linkWeight = re.match(settings.linkPattern, line).group(3)
                if validateLinkData(linkNode1, linkNode2, linkWeight, nodeDict, settings):
                    node1 = nodeDict[linkNode1]
                    node2 = nodeDict[linkNode2]
                    #create Link
                    linkClass(node1, node2, linkWeight)


