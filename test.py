import json
import os
from tkinter import *
from tkinter.messagebox import showinfo

import Calculation_module.calculateOrder as Cal
import Calculation_module.initModel as initM
from FileIO.fileIO import *
from FileIO.fileStructure import *
from UI.MainPage import *
from UI.view_ShowAnsList import *
# to=Cal.dfs_Search(initM.initData(5,5))

# to.PrintDfsResult()
# print(to.retMinTimeAns().transClassToString())


# Cal.dfs_Search(initM.testData(2,2,[[1,0],[0,1]],[100,100],[[5,0],[0,6]],[[2,0],[0,3]],[[2,0],[0,2]]))


# print(os.path.normpath(os.path.join(saveRoad,'a.json')))

# with open(os.path.abspath(os.path.join(saveRoad,'a.json')), 'w', encoding='utf-8') as f:
#     json.dump(to,f, default=lambda o: o.__dict__)


# print(getFlagLoad_byFile(os.path.join(saveRoad,'a.json')))

'测试originPage'
if   True:
    root = Tk()
    root.title("银行家算法")
    MainPage(root)
    root.mainloop()

'测试资源显示'
if      False:
    ResoDetail(initData()).showPage()

'test ShowAnsList'
if      not     True:
    for i in range(10):
        ShowAnslist(dfs_Search(initData())).showPage()

'test read File'
if     not    True:
    a=getFlagLoad_byFile(get_saveRoad_absPath('save_2'))


'test save file'
if     not      True:
    pushAnslist_ToFile(dfs_Search(initData()), 'save_2')

'test show'
if    not   True:
    pt=2
    insertString="\n本次用时较长"
    showinfo('info',f'''计算完成,用时:{pt:.2f}{insertString if pt>3 else ""}
打开答案详情界面''')
    #{"\n本次用时较长" if self.ansClass.retRunTime_second()>3 else ""}

