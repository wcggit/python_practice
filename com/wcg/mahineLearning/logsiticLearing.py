# coding=UTF-8
from numpy import *
import math


def loadDataSet():
    dataSet = []
    dataLable = []
    fl = open("testSet.txt")
    for line in fl.readlines():
        line = line.strip().split("	")
        dataSet.append([1.0,1.0,float(line[0]), float(line[1])])
        dataLable.append(int(line[2]))
    return dataSet, dataLable


def sigmoid(x):
    return 1.0 / (1 + exp(-x))


def gradientAscent(trainDataSet, lableData):  # w:=w+α(y(i) −hw(x(i)) x(i)
    trainMat = mat(trainDataSet)
    trainLable = mat(lableData).transpose()
    w = mat(ones((trainMat.shape[1], 1)))
    alpha = 0.001  # 步长
    for i in range(500):  # 走500步
        error = trainLable - sigmoid(trainMat * w)
        w = w + alpha * trainMat.transpose() * error
    return w


if __name__ == '__main__':
    dataSet, dataLable = loadDataSet()
    w = gradientAscent(dataSet, dataLable)
    error = 0;
    index = 0;
    for data in dataSet:
        if sigmoid(data * w) > 0.5:
            if dataLable[index] != 1:
                error += 1
            else:
                print True
        else:
            if dataLable[index] == 1:
                error += 1
            else:
                print True
        index += 1
    print error
    print float(error) / len(dataSet)
