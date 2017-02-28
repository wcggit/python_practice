class wayNode:
    def __init__(self, x, y, parent, son1, son2, isEnd=False):
        self.x = x
        self.y = y
        self.parent = parent
        self.son1 = son1
        self.son2 = son2
        self.isEnd = isEnd

    def isEnd(self):
        return self.isEnd


def findSon(node, header):
    if (node.x + 1 <= 6):
        node.son1 = 1
        if (node.y == 6 & node.x + 1 == 6):
            node.son1 = wayNode(node.x + 1, node.y, node, None, None, True)
            header.append(node.son1)
        else:
            node.son1 = wayNode(node.x + 1, node.y, node, None, None, False)
            findSon(node.son1, header)
    if (node.y + 1 <= 6):
        if (node.x == 6 & node.y + 1 == 6):
            node.son2 = wayNode(node.x, node.y + 1, node, None, None, True)
            header.append(node.son2)
        else:
            node.son2 = wayNode(node.x, node.y + 1, node, None, None, False)
            findSon(node.son2, header)


def calculaValue(node, v):
    if (node.x == 0 & node.y == 0):
        return v
    else:
        v += node.x
        v += node.y
        return calculaValue(node.parent, v)


if __name__ == '__main__':
    node = wayNode(0, 0, None, None, None)
    header = []
    findSon(node, header)
    bigV = 0;
    bigLine = None;
    for endNode in header:
        v = 0
        v = calculaValue(endNode.parent, v)
        print v
        if bigV <= v:
            bigV = v
            bigLine = endNode;
    print bigV
