# coding=UTF-8
import copy
from functools import partial


def choseNextNode(node, data, times, statistic):
    if times == 0:
        statistic[0] += 1
        return
    calSet = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1), (1, 2), (2, 1), (-1, -2), (-2, -1),
              (-1, 2), (-2, 1), (1, -2), (2, -1)]
    for cal in calSet:
        nextNode = tuple(map(sum, zip(node, cal)))
        if nextNode in data:
            newData = copy.copy(data)
            newData.remove(nextNode)
            choseNextNode(node, newData, times - 1, statistic)


def nine():
    statistic = [0]
    dataSet = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for i in range(2, 10):
        for nodeS in (dataSet):
            dt = copy.copy(dataSet)
            dt.remove(nodeS)
            len = i - 1
            choseNextNode(nodeS, dt, len, statistic)
    return statistic


from itertools import chain, permutations

impossible = {'13': '2',
              '46': '5',
              '79': '8',
              '17': '4',
              '28': '5',
              '39': '6',
              '19': '5',
              '37': '5',
              '31': '2',
              '64': '5',
              '97': '8',
              '71': '4',
              '82': '5',
              '93': '6',
              '91': '5',
              '73': '5'}


def counts():
    iterlst = chain(*(permutations('123456789', i) for i in range(4, 10)))
    count = 0
    for i in iterlst:
        stri = ''.join(i)
        for k, v in impossible.items():
            if k in stri and v not in stri[:stri.find(k)]:
                break
        else:
            count += 1
    return count


def vector_add(v, w):
    print v, w
    return [v_x + w_x for v_x, w_x in zip(v, w)]


if __name__ == '__main__':
    
    print zip((1, 2), (3, 4), (5, 6))
print reduce(vector_add, ((1, 2), (3, 4), (5, 6)),[3,3])
