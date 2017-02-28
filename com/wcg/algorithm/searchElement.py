# coding=UTF-8
def binarySearch(dataSet, value):  # 二分查找
    low = 0
    high = len(dataSet) - 1
    while low <= high:
        mid = (high + low) / 2
        if dataSet[mid] > value:
            high = mid - 1
        elif dataSet[mid] < value:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    print binarySearch([1, 2, 3, 4, 5, 6, 7], 8)
