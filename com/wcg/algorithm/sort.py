# coding=UTF-8
# 直接插入排序
import time
from math import ceil


def insert_sorts(dataSet):
    for i in range(1, len(dataSet)):
        val = dataSet[i]
        j = i - 1
        while (j >= 0) and (dataSet[j] > val):
            dataSet[j + 1] = dataSet[j]
            j = j - 1
        dataSet[j + 1] = val
    return dataSet


def shell_sorts(data, d):  # 希尔排序
    d = len(data)
    while True:
        d = int(ceil(d / 2))
        for i in range(0, d):
            j = i + d
            while j < len(data):
                dt = data[j]
                z = j - d
                while (z >= 0) and (data[z] > dt):
                    data[z + d] = data[z]
                    z -= d
                data[z + d] = dt
                j += d
        if d == 1:
            break
    return data


if __name__ == '__main__':
    ts = time.time()
    print insert_sorts([10, 20, 8, 25, 35, 6, 18, 30, 5, 15, 28])
    ts2 = time.time()
    print  shell_sorts([10, 20, 8, 25, 35, 6, 18, 30, 5, 15, 28], 3)
    ts3 = time.time()
    print  ts2-ts,ts3-ts2
