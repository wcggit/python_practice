# coding=UTF-8
from numpy import *


def loadSimpData():
    datMat = matrix([[1., 2.1],
                     [2., 1.1],
                     [1.3, 1.],
                     [1., 1.],
                     [2., 1.]])
    # classLabels = [[1.0], [1.0], [-1.0], [-1.0], [1.0]]
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat, classLabels


def classifyByThreshold(dataMatrix, index, threshold, inequality):  # 参数1 数据集，2 类别的索引 3 阈值 4 大于或者小于 返回根据阈值分类类别
    returnLable = ones((dataMatrix.shape[0], 1))  # 初始化返回矩阵
    if inequality == 'lt':  # 小于阈值
        returnLable[dataMatrix[:, index] <= threshold] = -1
    else:
        returnLable[dataMatrix[:, index] > threshold] = -1
    return returnLable


def createDescisionStump(dataMatrix, classifyLables, D):  # 简单决策树 D 代表各个属性的权重  返回最佳分类属性 最佳阈值 ，最佳错误率，阈值分类
    numStep = 10.0  # 阈值分类步长
    lables = mat(classifyLables).T
    minError = inf  # 初始化最小错误率 为无穷大
    dimen = {}  # 返回的分类属性，阈值
    returnLable = mat(zeros((dataMatrix.shape[1], 1)));  # 返回对分类lable
    for i in range(dataMatrix.shape[1]):  # 对每列属性进行循环
        minFeature = dataMatrix[:, i].min()  # 获取当前属性对最大最小值计算阈值
        maxFeature = dataMatrix[:, i].max()
        threaStep = (maxFeature - minFeature) / numStep  # 阈值间隔
        for j in range(-1, int(numStep)):  # 对阈值进行循环
            for ineq in ['lt', 'gt']:
                threahold = minFeature + threaStep * j
                predictLable = classifyByThreshold(dataMatrix, i, threahold, ineq)  # 根据阈值进行对分类
                errLable = mat(ones((dataMatrix.shape[0], 1)))
                errLable[predictLable == lables] = 0
                currentError = D.T * errLable  # 考虑权重的错误率
                if minError > currentError:
                    minError = currentError
                    dimen['index'] = i
                    dimen['ineq'] = ineq
                    dimen['threahold'] = threahold
                    returnLable = predictLable.copy()
    return dimen, minError, returnLable


#

def adaBoostTrainDS(dataArr, classLabels, numIt=40):
    weakClassArr = []
    m = shape(dataArr)[0]
    D = mat(ones((m, 1)) / m)  # init D to all equal
    aggClassEst = mat(zeros((m, 1)))
    for i in range(numIt):
        bestStump, error, classEst = createDescisionStump(dataArr, classLabels, D)  # build Stump
        # print "D:",D.T
        alpha = float(
            0.5 * log((1.0 - error) / max(error, 1e-16)))  # calc alpha, throw in max(error,eps) to account for error=0
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)  # store Stump Params in Array
        # print "classEst: ",classEst.T
        expon = multiply(-1 * alpha * mat(classLabels).T, classEst)  # exponent for D calc, getting messy
        D = multiply(D, exp(expon))  # Calc New D for next iteration
        D = D / D.sum()
        # calc training error of all classifiers, if this is 0 quit for loop early (use break)
        aggClassEst += alpha * classEst
        # print "aggClassEst: ",aggClassEst.T
        aggErrors = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m, 1)))
        errorRate = aggErrors.sum() / m
        print "total error: ", errorRate
        if errorRate == 0.0: break
    return weakClassArr, aggClassEst


def buildStump(dataArr, classLabels, D):
    dataMatrix = mat(dataArr);
    labelMat = mat(classLabels).T
    m, n = shape(dataMatrix)
    numSteps = 10.0;
    bestStump = {};
    bestClasEst = mat(zeros((m, 1)))
    minError = inf  # init error sum, to +infinity
    for i in range(n):  # loop over all dimensions
        rangeMin = dataMatrix[:, i].min();
        rangeMax = dataMatrix[:, i].max();
        stepSize = (rangeMax - rangeMin) / numSteps
        for j in range(-1, int(numSteps) + 1):  # loop over all range in current dimension
            for inequal in ['lt', 'gt']:  # go over less than and greater than
                threshVal = (rangeMin + float(j) * stepSize)
                predictedVals = classifyByThreshold(dataMatrix, i, threshVal,
                                                    inequal)  # call stump classify with i, j, lessThan
                errArr = mat(ones((m, 1)))
                errArr[predictedVals == labelMat] = 0
                weightedError = D.T * errArr  # calc total error multiplied by D
                # print "split: dim %d, thresh %.2f, thresh ineqal: %s, the weighted error is %.3f" % (i, threshVal, inequal, weightedError)
                if weightedError < minError:
                    minError = weightedError
                    bestClasEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestClasEst


def adaClassify(datToClass, classifierArr):
    dataMatrix = mat(datToClass)  # do stuff similar to last aggClassEst in adaBoostTrainDS
    m = shape(dataMatrix)[0]
    aggClassEst = mat(zeros((m, 1)))
    print range(len(classifierArr))
    for i in range(len(classifierArr)):
        print classifierArr[i]
        print classifierArr[i]['index']
        print classifierArr[i]['threahold']
        print classifierArr[i]['ineq']
        classEst = classifyByThreshold(dataMatrix, classifierArr[i]['index'], classifierArr[i]['threahold'],
                                        classifierArr[i]['ineq'])  # call stump classify
        aggClassEst += classifierArr[i]['alpha'] * classEst
        print aggClassEst
    return sign(aggClassEst)


if __name__ == '__main__':
    dataMatrix, lables = loadSimpData()
    print adaClassify([[0, 1],[2,2]],adaBoostTrainDS(dataMatrix, lables)[0])
