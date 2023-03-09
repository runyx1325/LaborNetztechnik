def validateNodeData(nodeName, nodeID):
    return validateNodeName(nodeName) and validateNodeID(nodeID)

def validateLinkData(linkNode1, linkNode2, linkWeight):
    return validateLink(linkNode1, linkNode2) and validatelinkWeight(linkWeight)

def validateNodeName(nodeName):
    #check if this name already exists
    #if not we have to create this node if maximum of items is not reached (MAX_ITEMS)
    return True

def validateNodeID(nodeID):
    #node ID has to be bigger then 0 and smaller then MAX_NODE_ID
    #at the end we have to check if there are more then one smallest ID
    return True

def validatelinkWeight(linkWeight):
    #maximum of Weight has to be MAX_KOSTEN
    #minimum of Weight has to be 1
    #if weight is 0 ignore this link
    return True

def validateLink(linkNode1, linkNode2):
    #check if linkNodes exists or we have to create
    #no link to themself, linkNode1 and linkNode2 has to be diffrent
    pass