# coding=UTF-8

def loadDateSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


def createCl(D):  # 数据集切割，获取所有的数据集
    sorted = []
    for data in D:
        for item in data:
            if [item] not in sorted:
                sorted.append([item])
    return map(frozenset, sorted)


def filterFeatureByMinSupport(Data, cl, minSupport=0.5):  # 过滤特征通过minSupport
    featureList = {}
    returnFeature = [];
    numbers = float(len(Data))
    supports = {}
    for data in Data:
        for item in cl:
            if item.issubset(data):
                featureList[item] = featureList.get(item, 0) + 1
    for key in featureList:
        support = featureList[key] / numbers
        if support >= minSupport:
            returnFeature.append(key)
            supports[key] = support
    return returnFeature, supports


# 生成组合特征 比如 {0},{1},{2} 返回 {0,1},{0,2},{1,2} k 是为了减少计算量，比如输入 {0,1},{0,2},{1,2}会返回{0,1,2} 但是如果没有K需要计算 3次 ，，如果有K 只需要计算一次就可以得到{0,1,2}
def aprioriGen(ck, k):
    length = len(ck);
    returnFeature = []
    for i in range(length):
        for j in range(i + 1, length):
            l1 = list(ck[i])[:k - 2].sort()
            l2 = list(ck[j])[:k - 2].sort()
            if l1 == l2:
                returnFeature.append(ck[i] | ck[j])
    return returnFeature


def apriori(dataSet, minSupport):  # 根据minsupport 返回特征集 与各特征集的support
    initCk, supports = filterFeatureByMinSupport(dataSet, createCl(dataSet), minSupport)
    lk = [initCk]
    k = 2
    while lk[k - 2] != []:
        ck, currentSupports = filterFeatureByMinSupport(dataSet, aprioriGen(lk[k - 2], k), minSupport)
        lk.append(ck)
        supports.update(currentSupports)
        k += 1
    return lk,supports


if __name__ == '__main__':
    dataSet = map(frozenset, loadDateSet());
    print apriori(dataSet,0.5)
