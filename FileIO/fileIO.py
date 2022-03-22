import json
import os

from Calculation_module.calculateOrder import ansRecord, base_AnsClass, dfs_Search, record
from Calculation_module.initModel import baseData
from FileIO.fileStructure import *


def pushAnslist_ToFile(to: dfs_Search, toName):
    "将to存储在名为toName的文件中"
    with open(get_saveRoad_absPath(toName), 'w', encoding='utf-8') as f:
        json.dump(to, f, default=lambda o: o.__dict__)


def getFlagLoad_byFile(toNamePath) -> tuple:
    "读取文件获得Data和anslist"
    def jsonToClass(xDict: dict):
        if 'ClassName' in xDict:
            if xDict['ClassName'] == 'record':
                return record(xDict['clientList'], xDict['beginTimeList'])
            elif xDict['ClassName'] == 'ansRecord':
                return ansRecord(xDict['finalRecord'], xDict['endTime'])
            elif xDict['ClassName'] == 'AnsClass':
                return base_AnsClass(xDict['orignData'], xDict['anslist'])
            elif xDict['ClassName'] == 'Data':
                return baseData(xDict['clientNum'], xDict['resoNum'], xDict['boolNeed'], xDict['haveResoList'], xDict['allocatedList'], xDict['TimeList'], xDict['NeedList'])
    with open(toNamePath, 'r', encoding='utf-8') as f:
        return json.load(f, object_hook=jsonToClass)


def detectDuplicateName_ansjson(toName):
    "查看是否重名,若有return True"
    return os.path.exists(get_saveRoad_absPath(toName))


def detectPathExist(absPath):
    "根据绝对路径查看是否存在"
    return os.path.exists(absPath)


def findNoDuplicateName(toName):
    "寻找不重名的文件, --返回的文件名可能仍然重名"
    ch = toName
    for i in range(1, int(1e3)):
        ch = toName+'_'+str(i)
        if not os.path.exists(get_saveRoad_absPath(ch)):
            break
    return ch
