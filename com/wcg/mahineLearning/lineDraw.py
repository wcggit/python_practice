if __name__ == '__main__':
    n = input("enter a number ")
    dataSet = []
    for i in range(n):
        data = raw_input()
        spotArr = sorted([data.split(" ")[0:2], data.split(" ")[2:]], key=lambda d: d[0])
        line = {"spot": spotArr, "k": (
                                          float(spotArr[1][1]) - float(spotArr[0][1])) / (
                                          float(spotArr[1][0]) - float(spotArr[0][0]))}
        lineExist = [d
                     for d in dataSet if float(d["k"]) == float(line["k"])]

        if (len(lineExist) != 0):
            xArea = range(int(spotArr[0][0]), int(spotArr[1][0]) + 1)
            xExit = range(int(lineExist[0]["spot"][0][0]), int(lineExist[0]["spot"][1][0]) + 1)
            xArea.extend(xExit)
            s = set(xArea)
            if (len(s) == len(xArea)):
                dataSet.append(line)
        else:
            dataSet.append(line)
    print len(dataSet)
