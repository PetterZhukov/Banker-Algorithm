import copy
import time

from Calculation_module.initModel import *
from Calculation_module.baseCalculate import *
from Constant.constant import *

sec_Max = 1e6
ansList_maxLen=1500

class record:
    '记录 当前那些客户开始释放以及释放的时间'

    def __init__(self, clientList=[], beginTimeList=[]) -> None:
        self.ClassName = 'record'
        self.clientList = clientList
        '开始释放的客户名list'
        self.beginTimeList = beginTimeList
        '记录开始时间'

    def retClientList(self):
        return self.clientList

    def retBeginTimeList(self):
        return self.beginTimeList

    def retAppendElementSelf(self, clientName, beginTime):
        'ret 一个添加记录的self'
        temp_self = copy.deepcopy(self)
        temp_self.clientList.append(clientName)
        temp_self.beginTimeList.append(beginTime)
        return temp_self

    def defineClientInList(self, clientName):
        '客户是否已经被释放 True:已被释放且被记录'
        return clientName in self.clientList

class ansRecord:
    '记录最终结果'

    def __init__(self, finalRecord: record, endTime) -> None:
        self.ClassName = 'ansRecord'
        self.finalRecord = finalRecord
        '最后的record'
        self.endTime = endTime
        '结束时间'

    def retFinalRecord(self):
        return self.finalRecord

    def retEndTime(self):
        return self.endTime

class base_AnsClass:
    def __init__(self, orignData: baseData, anslist) -> None:
        self.ClassName = 'AnsClass'
        # 初始Data
        self.orignData = orignData
        # anslist
        self.anslist = anslist
        self.clientNum, self.resoNum = orignData.clientNum, orignData.resoNum

    def retOrignData(self):
        return self.orignData

    def retAnsNum(self):
        return len(self.anslist)

    def retAnsList(self):
        return self.anslist

    def retMinTimeAns(self) -> ansRecord:
        return self.anslist[0]


class dfs_Search(base_AnsClass):
    def __init__(self, Data: initData) -> None:
        # 初始Data
        self.ClassName = 'AnsClass'
        self.orignData = Data

        # anslist
        self.anslist = []

        self.clientNum, self.resoNum = Data.clientNum, Data.resoNum
        self.clientPartSum = listGetSum(
            Data.boolNeed, self.clientNum, self.resoNum)
        timeTableList = [
            [-1000 for j in range(self.resoNum)]for i in range(self.clientNum)]
        # calculate time
        time_start = time.time()
        # dfs
        self.calculate_dfs(1, 0, record(),  timeTableList, Data)
        # sort
        self.sort_anslist()
        # 程序片段后插入以下两行
        time_end = time.time()
        self.runTime = time_end - time_start

    def retRunTime_second(self):
        return self.runTime

    def sort_anslist(self):
        self.anslist.sort(key=lambda ans: ans.endTime)

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

        #超过设定最大条数，结束dfs
        if len(self.anslist)>=ansList_maxLen:
            return

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
