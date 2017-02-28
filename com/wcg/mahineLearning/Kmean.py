# coding=UTF-8
import operator
from numpy import *
import matplotlib
import matplotlib.pyplot as plt


def kmeanOf(target, dataSets, lables, k):
    distanceSq = (tile(target, (dataSets.shape[0], 1)) - dataSets) ** 2  # 复制目标源并求出与测试数据的差的平方
    distanceArray = distanceSq.sum(axis=1) ** 0.5;  # 距离行相加后开方, 目标源与测试数据距离的数组
    distanceIndexSort = distanceArray.argsort();  # 升序索引
    countTarget = {}
    zeros
    for i in range(k):
        currentLable = lables[distanceIndexSort[i]];  # 获取当前距离的lable
        countTarget[currentLable] = countTarget.get(currentLable, 0) + 1;
    # 遍历 countTarget
    return sorted(countTarget.iteritems(), key=operator.itemgetter(1), reverse=True)[0][0]


def readFile(filename):
    file = open(filename);
    arrayLines = file.readlines();
    testMatrix = zeros((len(arrayLines), 3))
    testLablesVector = [];
    index = 0
    for line in arrayLines:
        line = line.strip().replace('\'', '');
        lineLists = line.split('   ');
        testMatrix[index, :] = lineLists[0:3]
        testLablesVector.append(str(lineLists[-1]));
        index += 1
    return testMatrix, testLablesVector


def autoNorm(dataSet):  # newValue = oldValue - min / max-min
    max = dataSet.max(0)  # 每一列的最大值，返会一个一维数组，元素与矩阵的列数相同 0 代表axis = 0 如果
    min = dataSet.min(0)
    minTile = tile(min, (int(dataSet.shape[0]), 1))
    maxTile = tile(max, (int(dataSet.shape[0]), 1))
    newDataSet = array((dataSet - minTile),dtype=float) / array((maxTile - minTile),dtype=float)
    return newDataSet, array(max - min,dtype=float), array(min,dtype=float)


if __name__ == '__main__':
    # print kmeanOf([4,4,1],readFile("test.txt")[0],readFile("test.txt")[1],1)
    # matrix = readFile("test.txt")[0];
    # arrays = readFile("test.txt")[1];
    # ax = plt.figure().add_subplot(111);
    # ax.scatter(matrix[:, 1], matrix[:, 2], 15, 30)
    # plt.show()
    dataSets = autoNorm(array([[11, -1], [1, 2], [2, 0], [2, 1], [1, 0]]))
    print dataSets[1]
    print dataSets[2]
    print dataSets[0]
    print kmeanOf((array([2, 0]) - dataSets[2]) / dataSets[1], dataSets[0], ['a', 'a', 'b', 'b', 'a'], 1)
    print kmeanOf((array([[2, 0]]) - dataSets[2]) / dataSets[1], dataSets[0], ['a', 'a', 'b', 'b', 'a'], 1)
    print linalg.solve(mat([[0,1,2],[1,1,4],[2,-1,0]]),mat([[1,0,0],[0,1,0],[0,0,1]]))