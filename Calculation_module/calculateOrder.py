import copy

from Calculation_module.initModel import *
from Calculation_module.baseCalculate import *
from Constant.constant import *

sec_Max = 1e6



class record:
    '记录 当前那些客户开始释放以及释放的时间'

    def __init__(self) -> None:
        self.clientList = []
        '开始释放的客户名list'
        self.beginTimeList = []
        '记录开始时间'

    def retAppendElementSelf(self, clientName, beginTime):
        'ret 一个添加记录的self'
        temp_self = copy.deepcopy(self)
        temp_self.clientList.append(clientName)
        temp_self.beginTimeList.append(beginTime)
        return temp_self

    def defineClientInList(self, clientName):
        '客户是否已经被释放 True:已被释放且被记录'
        return clientName in self.clientList

    def transClassToTuple(self):
        return tuple(zip(self.clientList, self.beginTimeList))
        # 假如超过26  -------------------------------------------
        # return zip(self.clientList, self.beginTimeList)

    def transClassToString(self):
        return tuple(zip(map(lambda x: numToAlp_dict[x], self.clientList), map(lambda x: f"{x:>2}", self.beginTimeList)))


class ansRecord:
    '记录最终结果'

    def __init__(self, finalRecord: record, endTime) -> None:
        self.finalRecord = finalRecord
        '最后的record'
        self.endTime = endTime
        '结束时间'

    def transClassToTuple(self):
        return (self.finalRecord.transClassToTuple(), self.endTime)

    def transClassToString(self):
        return(
            f'{self.finalRecord.transClassToString()}   end={self.endTime}')


class dfs_Search:
    def __init__(self, Data: initData) -> None:
        self.orignData=Data

        # dfs
        clientNum, resoNum = Data.clientNum, Data.resoNum
        timeTableList = [
            [-1000 for j in range(resoNum)]for i in range(clientNum)]

        self.anslist = []
        self.clientPartSum = listGetSum(Data.boolNeed, clientNum, resoNum)
        self.calculate_dfs(1, 0, record(),  timeTableList, Data)
        
        #sort
        self.sort_anslist()

    def retMinTimeAns(self)->ansRecord:
        return self.anslist[0]

    def sort_anslist(self):
        self.anslist.sort(key=lambda ans:ans.endTime)

    def PrintDfsResult(self):
        for i, x in enumerate(self.anslist):
            print(f'{i+1:>3}  {x.transClassToString()}')

    def calculate_dfs(self, sec: int, releasedResoNum, recordList: record, timeTableList, Data: initData):
        '''
        sec:当前是第几秒,
        recordList:记录顺序,[(开始时间,序号)]
        usedList[][]:i客户的j资源是否被释放  True是已经释放,
        timeTableList[][]: i客户 j资源 = 资源释放时刻,
        Data:数据存放处
        '''
        clientNum = Data.clientNum
        resoNum = Data.resoNum

        if sec >= sec_Max:
            return
        # 更新Data，有可以释放的资源就释放掉
        for i in range(clientNum):
            for j in range(resoNum):
                if timeTableList[i][j] > 0 and sec >= timeTableList[i][j]:
                    # 释放
                    Data.haveResoList[j] += (Data.allocatedList[i]
                                             [j]+Data.NeedList[i][j])
                    # update timeTableList
                    timeTableList[i][j] = -1000
                    # update releasedResoNum
                    releasedResoNum += 1

        if releasedResoNum == self.clientPartSum:
            # 全部释放
            self.anslist.append(ansRecord(recordList, sec))
            return

        haveReleaseClient = False

        for i in range(Data.clientNum):
            if not recordList.defineClientInList(i) and list_compare(Data.NeedList[i], Data.haveResoList, resoNum):
                # 开始计时
                # 仍然需求要扣掉
                temp_Data = copy.deepcopy(Data)
                for j in range(resoNum):

                    temp_Data.haveResoList[j] -= Data.NeedList[i][j]

                # 加上倒计时
                temp_timeTableList = [[Data.TimeList[k][j]+sec if k == i and Data.boolNeed[k][j] else timeTableList[k][j]
                                       for j in range(resoNum)] for k in range(clientNum)]
                haveReleaseClient = True
                self.calculate_dfs(
                    sec+1, releasedResoNum, recordList.retAppendElementSelf(i, sec),  temp_timeTableList, temp_Data)
        if not haveReleaseClient:
            self.calculate_dfs(sec+1, releasedResoNum, recordList,
                               timeTableList, Data)
