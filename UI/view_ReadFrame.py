import os
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter.messagebox
import tkinter.filedialog

from Calculation_module.calculateOrder import dfs_Search
from FileIO.fileIO import detectDuplicateName_ansjson, detectPathExist, findNoDuplicateName, getFlagLoad_byFile
from UI.view_ShowAnsList import ShowAnslist
import FileIO.fileStructure
from UI.view_ShowResoDetail import ResoDetail

class ReadFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master

        self.clientNumVar = StringVar()
        self.resoNumVar = StringVar()
        self.showReadNameVar = StringVar()
        self.readFilePath=''
        self.Data = None
        self.ansClass = None

        self.haveReadFile=False
        
        self.creatPage()

    def creatPage(self):
        row = 0
        Label(self).grid(row=row)

        row += 1
        Label(self, text="读取记录的安全路径",
              font=('宋体', 20, 'bold'))\
            .grid(row=row, column=0, columnspan=4)

        row += 1
        ttk.Separator(self, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(self, text="读取名", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)
        Entry(self, textvariable=self.showReadNameVar,state='disable').grid(
            row=row, column=1, sticky=W)
        Button(self, text="选择文件", command=self.getName_saveResult).grid(
            row=row, column=2, padx=10, pady=3, sticky=EW)

        row += 1
        Button(self, text="读取文件", command=self.readFile).grid(
            row=row, column=2, padx=10, pady=5, sticky=EW)


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
        Button(self, text="显示初始化详细信息", command=self.showInitDetails).grid(
            row=row, column=1, padx=10,pady=5,sticky=EW)

        row += 1
        Button(self, text="显示安全序列详情", command=self.calculateAns_OpenDetail).grid(
            row=row, column=1, padx=10,sticky=EW)

        


    def checkRead(self):
        '检查是否已经读取'
        if not self.haveReadFile:
            tkinter.messagebox.showwarning('提示', '请先读取文件')
            return False
        return True

    def getName_saveResult(self):
        self.readFilePath=(tkinter.filedialog.askopenfilename(initialdir=FileIO.fileStructure.saveRoad))
        self.showReadNameVar.set(self.readFilePath.split('/')[-1])


    def showInitDetails(self):
        # 判断是否初始化
        if self.checkRead():
            ResoDetail(self.Data).showPage()

    def calculateAns_OpenDetail(self):
        # 判断是否初始化
        if self.checkRead():
            # 打开详情页面
            ShowAnslist(self.ansClass).showPage()
    
    def readFile(self):
        # 读取json文件,构建类
        if not detectPathExist(self.readFilePath):
            tkinter.messagebox.showerror('警告','文件不存在,请重新选择')
        else:
            self.ansClass=getFlagLoad_byFile(self.readFilePath)
            self.Data=self.ansClass.retOrignData()
            self.haveReadFile=True
            tkinter.messagebox.showinfo('提示','读取成功')
            self.clientNumVar.set(self.Data.returnClientNum())
            self.resoNumVar.set(self.Data.returnResoNum())
        

    