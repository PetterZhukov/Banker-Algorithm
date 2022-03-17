

def list_sum_2(clintList: list, haveList: list, clientNum, resoNum):
    "矩阵相加"
    return [[clintList[i][j]+haveList[i][j] for j in range(resoNum)] for i in range(clientNum)]


def list_sub(clintList: list, haveList: list, clientNum, resoNum):
    "矩阵相减"
    return [[clintList[i][j]-haveList[i][j] for j in range(resoNum)] for i in range(clientNum)]


def list_sum_1(clintList: list, haveList: list, resoNum):
    "一维矩阵+一维矩阵"
    return [clintList[j]+haveList[j] for j in range(resoNum)]


# def list1_Add_list2(list1: list, list2: list, row, clientNum, resoNum):
#     '一维矩阵+二维矩阵 第row行'
#     return [[list1[j]+list2[i][j] if i == row else list2[i][j] for j in range(resoNum)] for i in range(clientNum)]


def list_compare(clintList: list, haveList: list, resoNum: int):
    "当前剩余资源能否满足客户的需求 True:能"
    for i in range(resoNum):
        if clintList[i] > haveList[i]:
            return False
    return True

def listGetSum(tolist,clientNum, resoNum):
    '矩阵求和'
    sum=0
    for i in range(clientNum):
        for j in range(resoNum):
            sum+=tolist[i][j]
    return sum
