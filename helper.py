def validateNodeData(nodeName, nodeID, nodeDict, settings):
    return validateNodeName(nodeName, nodeDict) and validateNodeID(nodeID, settings)


def validateLinkData(linkNode1, linkNode2, linkWeight, nodeDict, settings):
    return validateLink(linkNode1, linkNode2, nodeDict) and validatelinkWeight(linkWeight, settings)


def validateNodeName(nodeName, nodeDict):
    # check if this name already exists
    return nodeName is not nodeDict
    # if not we have to create this node


def validateNodeID(nodeID, settings):
    # node ID has to be bigger than 0 and smaller than MAX_NODE_ID
    return 0 < nodeID < settings.MAX_NODE_ID
    # at the end we have to check if there are more than one smallest ID


def validatelinkWeight(linkWeight, settings):
    return settings.MAX_KOSTEN >= linkWeight >= 1
    # maximum of Weight has to be MAX_KOSTEN
    # minimum of Weight has to be 1
    # if weight is 0 ignore this link


def validateLink(linkNode1, linkNode2, nodeDict):
    return linkNode1 in nodeDict and linkNode2 in nodeDict and linkNode1 != linkNode2
    # check if linkNodes exists, or we have to create
    # no link to themselves, linkNode1 and linkNode2 has to be different
