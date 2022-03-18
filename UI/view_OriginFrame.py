import os
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter.messagebox

from Calculation_module.initModel import initData
from Calculation_module.calculateOrder import dfs_Search
from FileIO.fileIO import detectDuplicateName_ansjson, findNoDuplicateName, pushAnslist_ToFile
from UI.view_ResoDetail import ResoDetail


class OriginFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.clientNumVar = StringVar()
        self.resoNumVar = StringVar()
        self.saveNameVar = StringVar()
        self.Data = None
        self.anslist = None

        # flag
        self.haveInit = False
        self.haveCalculate = False

        self.creatPage()

    def creatPage(self):
        row = 0
        Label(self).grid(row=row)

        row += 1
        Label(self, text="银行家算法界面",
              font=('宋体', 20, 'bold'))\
            .grid(row=row, column=0, columnspan=4)

        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="客户数量", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)
        clientNumEntry = Entry(self, textvariable=self.clientNumVar)
        clientNumEntry['state'] = 'disabled'
        clientNumEntry.grid(row=row, column=1, sticky=W)

        row += 1
        Label(self, text="资源数量", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)
        resoNumEntry = Entry(self, textvariable=self.resoNumVar)
        resoNumEntry['state'] = 'disabled'
        resoNumEntry.grid(row=row, column=1, sticky=W)

        row += 1
        Button(self, text="开始随机生成", command=self.initData).grid(
            row=row, column=1, padx=10, pady=10, sticky=EW)

        Button(self, text="显示初始化详细信息", command=self.showInitDetails).grid(
            row=row, column=2, padx=10)

        row += 1
        Button(self, text="计算安全路径并显示详情", command=self.calculateAns).grid(
            row=row, column=1, padx=10)

        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="保存名", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)
        Entry(self, textvariable=self.saveNameVar).grid(
            row=row, column=1, sticky=W)

        row += 1
        Button(self, text="保存结果", command=self.saveAns).grid(
            row=row, column=1, padx=10, pady=10, sticky=EW)

    def checkInit(self):
        '检查是否已经初始化'
        if not self.haveInit:
            tkinter.messagebox.showwarning('提示', '请先初始化')
            return False
        return True

    def checkCalculate(self):
        '检查是否已经计算'
        if not self.haveInit:
            tkinter.messagebox.showwarning('提示', '请先计算安全路径')
            return False
        return True

    def initData(self):
        self.Data = initData()
        self.clientNumVar.set(self.Data.returnClientNum())
        self.resoNumVar.set(self.Data.returnResoNum())
        self.haveInit=True
        tkinter.messagebox.showinfo('提示', '初始化完成')

    def showInitDetails(self):
        # 判断是否初始化
        if self.checkInit():
            ResoDetail(self.Data).showPage()

    def calculateAns(self):
        # 判断是否初始化
        if self.checkInit():
            self.ansClass = dfs_Search(self.Data)
            self.haveCalculate=True
            tkinter.messagebox.showinfo('提示', '计算完成')

    def showAnsDetails(self):
        'show details of anslist'
        pass

    def saveAns(self):
        'save anslist in file'
        if self.checkCalculate():
            if detectDuplicateName_ansjson(self.saveNameVar.get()):
                newName = findNoDuplicateName(self.saveNameVar.get())
                if detectDuplicateName_ansjson(newName):
                    self.saveNameVar.set(newName)
                    tkinter.messagebox.showerror('警告', '选择的文件名重名,已更改为不重名的文件名')
                else:
                    tkinter.messagebox.showerror('警告', '要创建的文件和其他文件重名')
            else:
                pushAnslist_ToFile(self.ansClass, self.saveNameVar.get())
                tkinter.messagebox.showinfo('提示', '存储成功')

    