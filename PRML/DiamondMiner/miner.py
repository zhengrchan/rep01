import numpy as np

def dpminer(mine, size):
    # 初始化
    maxValue = np.zeros([size, size])
    maxWay = np.zeros([size, size])
    maxMoney = 0

    # 计算达到最大值经过的每一个子问题
    for i in range(size):
        maxValue[size - 1 - i][i] = mine[size - 1 - i][i]
    for i in range(size - 2, -1, -1):
        for j in range(i):
            maxValue[i - j][j] = mine[i - j][j] + max(maxValue[i - j + 1][j], maxValue[i - j][j + 1])

    # 计算达到最大值所需要经过的点
    maxWay[0][0] = 1
    j = 0
    k = 0
    for i in range(size - 1):
        if maxValue[j + 1][k] > maxValue[j][k + 1]:
            maxWay[j + 1][k] = 1
            j = j + 1
        else:
            maxWay[j][k + 1] = 1
            k = k + 1

    # 计算最大价值
    maxMoney = maxValue[0][0]

    return maxMoney, maxWay
