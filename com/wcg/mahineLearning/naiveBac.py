# coding=UTF-8
import operator
from numpy import *


def filterDataSet(dataSet):
    results = set();
    for data in dataSet:
        results = results | (set(data))
    return list(results)


def convertDataToVector(data, vector):
    results = zeros(len(vector))
    for value in data:
        results[vector.index(value)] = 1
    return results


def getClassifyProb(trainMat, trainClassify):  # 传入数据矩阵和分类，返回各个分类的概率和各属性在各分类的条件概率 P(Ci) P(W|Ci)
    types = list(set(trainClassify))
    results = {i: {} for i in types};
    for i in trainClassify:
        results[i][0] = results[i].get(0, 0) + 1
    for (key, data) in results.iteritems():
        print data
        data[0] = data[0] / float(len(trainClassify))  # 求各分类的P(Ci)
        data[1] = ones(len(trainMat[0]))  # 初始化各个类别中的出现的可能性，防止概率0的出现将初始化值设为1
        data[2] = 1.0  # 各类别的总数，相应的分母+1
    for i in range(len(trainMat)):
        pCi = results[trainClassify[i]]
        pCi[1] += trainMat[i]
        pCi[2] += sum(trainMat[i])
    for key, data in results.iteritems():
        data[1] = log(data[1] / data[2])  # 求对数防止 某个乘积为0
    return results


def showX(x):
    return (x[1][2], x[1][3])


def testBac(inputVector, trainDataProb):
    for key, value in trainDataProb.iteritems():
        value[3] = log(value[0]) + sum(inputVector * value[1])
    return sorted(trainDataProb.iteritems(), key=lambda x: showX(x), reverse=True)


if __name__ == '__main__':
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid'],
                   ['my', 'garbage', 'ss', '1', '2', '3', '4', '5', '6']]
    filterData = filterDataSet(postingList)
    print filterData
    trainMat = []
    for data in postingList:
        vect = convertDataToVector(data, filterData)
        trainMat.append(vect)

print testBac(convertDataToVector(['garbage', 'stupid'], filterData), getClassifyProb(trainMat, [0, 1, 0, 2, 0, 1, 2]))
