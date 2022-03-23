import random
import copy

# 固定范围
# 客户数
clientNum_max = 10
clientNum_min = 5
# 资源数
resourceNum_max = 30
resourceNum_min = 10
# 当前拥有的各个资源数量
haveResource_max = 200
haveResource_min = 140
# 各个客户各资源的时间
time_max = 30
time_min = 2
# 已分配资源的初始值
AllocatedResources_max = 70
AllocatedResources_min = 30
# 还需求的资源的初始值
NeedResources_max = 120
NeedResources_min = 80


def retRandomClientNum():
    return random.randint(clientNum_min, clientNum_max)


def retRandomResourceNum():
    return random.randint(resourceNum_min, resourceNum_max)


def retRandomHaveResourceSize():
    return random.randint(haveResource_min, haveResource_max)


def retRandomTime():
    return random.randint(time_min, time_max)


def retRandomAllocatedResources():
    return random.randint(AllocatedResources_min, AllocatedResources_max)


def retRandomStillNeedResources():
    return random.randint(NeedResources_min, NeedResources_max)

class baseData:
    def __init__(self, clientNum, resoNum, boolNeed, haveResoList, allocatedList, TimeList, NeedList) -> None:
        self.ClassName = 'Data'
        self.clientNum = clientNum
        self.resoNum = resoNum

        self.boolNeed = boolNeed
        '[i][j] i客户的j资源 是否需要'
        self.haveResoList = haveResoList
        '[j] 主机拥有的第j个资源'
        self.allocatedList = allocatedList
        '[i][j] i客户的j资源已分配数量'
        self.TimeList = TimeList
        '[i][j] i客户的j资源释放需要时间'
        self.NeedList = NeedList
        '[i][j] i客户的j资源还需资源'

    def returnClientNum(self):
        return self.clientNum

    def returnResoNum(self):
        return self.resoNum

    def retHaveResources(self):
        'ret 一个资源矩阵 第j列表示第j个资源的数量  当前主机拥有的资源数量'
        return [retRandomHaveResourceSize() for j in range(self.resoNum)]

    def retBoolNeed(self):
        'ret 一个bool矩阵,第i行第j列表示第i个客户是否需要第j类资源'
        return [[random.randint(0, 1) for j in range(self.resoNum)] for i in range(self.clientNum)]

    def changeHaveResources(self, haveResoList):
        '将拥有资源矩阵修改并返回self'
        ret = copy.deepcopy(self)
        ret.haveResoList = haveResoList
        return ret


class initData(baseData):

    def __init__(self, clientNum=None, resoNum=None) -> None:
        self.ClassName = 'Data'
        self.clientNum = clientNum if clientNum != None else retRandomClientNum()
        self.resoNum = resoNum if resoNum != None else retRandomResourceNum()

        self.boolNeed = self.retBoolNeed()
        '[i][j] i客户的j资源 是否需要'
        self.haveResoList = self.retHaveResources()
        '[j] 主机拥有的第j个资源'
        self.allocatedList = self.getAllocatedList()
        '[i][j] i客户的j资源已分配数量'
        self.TimeList = self.getTimeList()
        '[i][j] i客户的j资源释放需要时间'
        self.NeedList = self.getNeedList()
        '[i][j] i客户的j资源还需资源'

    def getAllocatedList(self):
        "已分配矩阵"
        return [[retRandomAllocatedResources()if self.boolNeed[i][j] else 0 for j in range(self.resoNum)] for i in range(self.clientNum)]

    def getTimeList(self):
        "所用时间矩阵"
        return [[retRandomTime() if self.boolNeed[i][j] else 0 for j in range(self.resoNum)] for i in range(self.clientNum)]

    def getNeedList(self):
        "仍然需求资源矩阵"
        return [[retRandomStillNeedResources()if self.boolNeed[i][j] else 0 for j in range(self.resoNum)] for i in range(self.clientNum)]
