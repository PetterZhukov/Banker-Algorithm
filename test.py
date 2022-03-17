import json
import os
import Calculation_module.calculateOrder as Cal
import Calculation_module.initModel as initM
from FileIO.fileStructure import *

to=Cal.dfs_Search(initM.initData(5,5))

to.PrintDfsResult()
print(to.retMinTimeAns().transClassToString())


# Cal.dfs_Search(initM.testData(2,2,[[1,0],[0,1]],[100,100],[[5,0],[0,6]],[[2,0],[0,3]],[[2,0],[0,2]])) 


# print(os.path.normpath(os.path.join(saveRoad,'a.json')))

# with open(os.path.abspath(os.path.join(saveRoad,'a.json')), 'w', encoding='utf-8') as f:
#     json.dump(to,f, default=lambda o: o.__dict__)