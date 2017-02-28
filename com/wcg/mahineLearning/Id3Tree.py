# coding=UTF-8
import operator
from numpy import *
from math import log
import com.wcg.treePlotter


def calEntropy(dataSet):
    countType = {}
    countLen = float(len(dataSet))
    entropy = 0.0
    for data in dataSet:
        countType[data[-1]] = countType.get(data[-1], 0) + 1
    for key in countType:
        probability = countType.get(key) / countLen
        entropy -= probability * log(probability, 2)
    return entropy


def splitDataSet(dataSet, axis, value):
    # 参数2 非类别属性 3 属性值 集合分类 返回会去除属性axis
    newDataSet = [];
    for data in dataSet:
        if data[axis] == value:
            splitData = list(data[:axis])
            splitData.extend(data[axis + 1:])
            newDataSet.append(splitData)  # extend 与 append 区别 [1,1,1,[3]] [1,1,1,3]
    return newDataSet


def defaultLableSelect(lableList):  # 如果决策树处理完毕所有的属性，但是类标签依旧不是唯一的，那么采用默认的类型选择
    sortedLableList = {}
    for lable in lableList:
        sortedLableList[lable] = sortedLableList.get(lable, 0) + 1
    return sorted(sortedLableList.iteritems(), key=operator.itemgetter(1), reverse=True)[0][0]


def calBestFeature(dataSet):
    baseEntropy = calEntropy(dataSet);  # 基础信息熵
    bestInfoGain = 0.0  # 基础信息增量
    bestFeature = -1
    featureNums = len(dataSet[0]) - 1  # 计算非类别属性总数
    for i in range(featureNums):  # 计算每个非类别的信息增量
        currentfeatureValues = set([example[i] for example in dataSet])  # 列表表达式,并去重
        currentEntropy = 0.0
        for currentFeaTure in currentfeatureValues:
            splitSet = splitDataSet(dataSet, i, currentFeaTure)
            currentEntropy += float(len(splitSet)) / len(dataSet) * calEntropy(splitSet)
        currentInfoGain = baseEntropy - currentEntropy;
        print currentInfoGain
        if (currentInfoGain > bestInfoGain):
            bestInfoGain = currentInfoGain
            bestFeature = i
    return bestFeature


def createTree(dataSet, treeLables):
    lableList = [example[-1] for example in dataSet]
    if lableList.count(lableList[0]) == len(lableList):  # 如果决策树中依旧没有别的类别，停止决策
        return lableList[0]
    if len(dataSet[0]) == 1:  # 没有属性决策，且类别不唯一
        return defaultLableSelect(lableList)
    bestFeatureIndex = calBestFeature(dataSet)
    bestFeature = treeLables[bestFeatureIndex]
    myTrees = {bestFeature: {}}
    del (treeLables[bestFeatureIndex])
    featureSet = set([example[bestFeatureIndex] for example in dataSet])  # 子节点
    for feature in featureSet:
        subLables = treeLables[:]  # 必须创建一个新的lables
        myTrees[bestFeature][feature] = createTree(splitDataSet(dataSet, bestFeatureIndex, feature), subLables)
    return myTrees


def testTree(tree, features, testValue):
    print tree
    splitFeature = tree.keys()[0]  # 获取第一个树节点
    spilitFeatureIndex = features.index(splitFeature)  # 找到相应的索引
    nodeValue = tree[splitFeature];  # 获取当前树节点的可能情况
    policy = nodeValue[testValue[spilitFeatureIndex]]  # 进行决策
    if type(policy).__name__ == 'dict':  # 说明要继续进行决策
        valueCategory = testTree(policy, features, testValue)
    else:
        valueCategory = policy
    return valueCategory;


if __name__ == '__main__':
    # print testTree( createTree(
    #      [[1, 0, 3, 'no'], [1, 2, 3, 'no'], [1, 1, 3, 'yes'], [1, 0, 6, 'no'], [0, 1, 3, 'maybe'], [0, 1, 6, 'no']],
    #      ['A', 'B', 'C']),['A','B','C'],[0,1,3])
    dict = {'B': {0: 'no', 1: {'A': {0: {'C': {3: 'maybe', 6: 'no'}}, 1: 'yes'}}, 2: 'no'}, 'c': 1}
    print type(dict).__dict__
    print type(dict).__name__
    print type(dict).__base__