from numpy import *
import operator

if __name__ == '__main__':
    matrix = eye(4)
    matrix2 = mat(random.rand(4, 4))
    groups = array([[1, 1], [1, 2], [2, 2], [2, 1], [1, 0]])
    lables = ['A', 'A', 'B', 'B', 'A']
    a = groups ** 2
    print a
    tile
    b = a.sum(axis=1);
    sortIndex = b.argsort()
    print sortIndex
    classCount = {}
    for i in range(4):
        voteLable = lables[sortIndex[i]]
        classCount[voteLable] = classCount.get(voteLable, 0) + 1
    for i in classCount.iteritems():
        print
    print sorted(classCount.iteritems(), key=operator.itemgetter(0), reverse=True)
    print zeros(10)
    print zeros((1,10))
