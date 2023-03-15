def validateNodeData(nodeName, nodeID, nodeDict, settings):
    return validateNodeName(nodeName, nodeDict) and validateNodeID(nodeID, settings)

def validateLinkData(linkNode1, linkNode2, linkWeight, nodeDict, settings):
    return validateLink(linkNode1, linkNode2, nodeDict) and validatelinkWeight(linkWeight, settings)

def validateNodeName(nodeName, nodeDict):
    #check if this name already exists
    return nodeName is not nodeDict
    #if not we have to create this node


def validateNodeID(nodeID, settings):
    #node ID has to be bigger then 0 and smaller then MAX_NODE_ID
    return nodeID > 0 and nodeID < settings.MAX_NODE_ID
    #at the end we have to check if there are more then one smallest ID

def validatelinkWeight(linkWeight, settings):
    return linkWeight <= settings.MAX_KOSTEN and linkWeight >= 1
    #maximum of Weight has to be MAX_KOSTEN
    #minimum of Weight has to be 1
    #if weight is 0 ignore this link

def validateLink(linkNode1, linkNode2, nodeDict):
    return linkNode1 in nodeDict and linkNode2 in nodeDict and linkNode1 != linkNode2
    #check if linkNodes exists or we have to create
    #no link to themself, linkNode1 and linkNode2 has to be diffrent