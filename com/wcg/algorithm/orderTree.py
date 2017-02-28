class treeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preOrder(node):
    print node.value
    if node.left != None:
        preOrder(node.left)
    if node.right != None:
        preOrder(node.right)


def midOrder(node):
    if node.left != None:
        midOrder(node.left)
    print node.value
    if node.right != None:
        midOrder(node.right)


def postOrder(node):
    if node.left != None:
        postOrder(node.left)
    if node.right != None:
        postOrder(node.right)
    print node.value


def searchTree(tree, v):
    if tree.value > v:
        if tree.right != None:
            searchTree(tree.left, v)
        else:
            return None
    elif tree.value < v:
        if tree.right!=None:
            searchTree(tree.right, v)
        else:
            return None
    else:
        return tree


if __name__ == '__main__':
    tree = treeNode('A', treeNode('B', treeNode('D', treeNode('G'), treeNode('H')), treeNode('E')),
                    treeNode('C', treeNode('K'), treeNode('F', treeNode('I', None, treeNode("J")))))
    preOrder(tree)
