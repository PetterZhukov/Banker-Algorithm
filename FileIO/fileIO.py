import json
import os

from Calculation_module.calculateOrder import dfs_Search
from FileIO.fileStructure import *

def pushAnslist_ToFile(to:dfs_Search,toName):
    "将to存储在名为toName的文件中"
    with open(get_saveRoad_absPath(toName), 'w', encoding='utf-8') as f:
        json.dump(to,f, default=lambda o: o.__dict__)

def getFlagLoad_byFile(toName)->tuple:
    "读取文件获得Data和anslist"
    with open(get_saveRoad_absPath(toName), 'r', encoding='utf-8') as f:
        info=json.load(f)
        return (info["orignData"],info["anslist"])

def detectDuplicateName_ansjson(toName):
    "查看是否重名"
    return os.path.exists(get_saveRoad_absPath(toName))

def findNoDuplicateName(toName):
    "寻找不重名的文件, --返回的文件名可能仍然重名"
    ch=toName
    for i in range(1, 1e3):
        ch=toName+'_'+str(i)
        if not os.path.exists(get_saveRoad_absPath(ch)):
            break
    return ch
