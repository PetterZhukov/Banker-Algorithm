import os
import tkinter.messagebox
from http import client
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

from Calculation_module.calculateOrder import ansRecord, dfs_Search
from Calculation_module.initModel import initData
from Constant.constant import numToAlp_dict

textlen = 7


def setTableText(master, toText, i, j):
    # 表格中第i行j列
    table = Text(master, width=textlen, height=2)
    table.insert("end", toText)
    table.grid(row=i, column=j)


class TableFrame1(Frame):
    def __init__(self, master, tableList, ResoNum):
        Frame.__init__(self, master)
        self.root = master
        self.ResoNum = ResoNum
        self.tableList = tableList
        self.__creatTable()

    def __creatTable(self):
        resoList = ['资源'+str(i) for i in range(1, self.ResoNum+1)]
        for j, resoName in enumerate(resoList):
            setTableText(self, resoName, 0, j+1)
        setTableText(self, '资源数', 1, 0)
        for j, t in enumerate(resoList):
            setTableText(self, f'{self.tableList[j]:>{textlen}}', 1, j+1)


class TableFrame2(Frame):
    def __init__(self, master, tableList, clientNum, resoName):
        Frame.__init__(self, master)
        self.root = master
        self.clientNum = clientNum
        self.resoName = resoName
        self.tableList = tableList
        self.__creatTable()

    def __creatTable(self):
        resoList = ['资源'+str(i) for i in range(1, self.resoName+1)]
        clientList = [numToAlp_dict[i] for i in range(self.clientNum)]
        for j, resoName in enumerate(resoList):
            setTableText(self, resoName, 0, j+1)

        for i, clientName in enumerate(clientList):
            setTableText(self, f'{clientName:>{textlen}}', i+1, 0)

        for j, t in enumerate(resoList):
            for i, num in enumerate(clientList):
                setTableText(
                    self, f'{self.tableList[i][j] if self.tableList[i][j]>0 else "x" :>{textlen}}', i+1, j+1)


class AnsDetail():
    def __init__(self, ansRecord:ansRecord):
        self.root = Tk()

        self.root.title("安全路径详情")

        # set the size

        self.creatScroAndTable()

    def showPage(self):
        self.root.mainloop()

    def creatScroAndTable(self):
        canvas = Canvas(master=self.root, width=int(
            (self.Data.resoNum+1)*(textlen*7.8)+20))
        scro = Scrollbar(master=self.root)
        # 滚动条
        scro.pack(side='right', fill='y')
        canvas.pack(side='left', fill='both')
        # Frame作为容器放置组件
        contentFrame = Frame(canvas)
        contentFrame.pack()
        # 将Frame添加至Canvas上
        canvas.create_window((0, 0), window=contentFrame, anchor="nw")

        # self.creatTable(frame)
        self.creatTable(contentFrame)
        # 更新Frame大小，不然没有滚动效果
        contentFrame.update()
        # 将滚动按钮绑定只Canvas上
        canvas.configure(yscrollcommand=scro.set,
                         scrollregion=canvas.bbox("all"))
        scro.config(command=canvas.yview)

    def creatTable(self, contentFrame):
        resoNum = self.Data.resoNum
        clientNum = self.Data.clientNum

        row = 0
        Label(contentFrame).grid(row=row)

        row += 1
        Label(contentFrame, text="资源细节",
              font=('宋体', 20, 'bold'))\
            .grid(row=row, column=0, columnspan=4)

        # --------------------------------------------------
        row += 1
        ttk.Separator(contentFrame, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(contentFrame, text="当前主机的资源数量", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)

        row += 1
        TableFrame1(contentFrame, self.Data.haveResoList, resoNum).grid(row=row,
                                                                        column=0,
                                                                        columnspan=10,
                                                                        pady=10,
                                                                        padx=15)

        # --------------------------------------------------
        row += 1
        ttk.Separator(contentFrame, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(contentFrame, text="已分配资源", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)

        row += 1
        TableFrame2(contentFrame, self.Data.allocatedList, clientNum, resoNum).grid(row=row,
                                                                                    stick=E,
                                                                                    column=0,
                                                                                    columnspan=10,
                                                                                    pady=10,
                                                                                    padx=15)
        # --------------------------------------------------
        row += 1
        ttk.Separator(contentFrame, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(contentFrame, text="客户使用资源需要的时间", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)

        row += 1
        TableFrame2(contentFrame, self.Data.allocatedList, clientNum, resoNum).grid(row=row,
                                                                                    stick=E,
                                                                                    column=0,
                                                                                    columnspan=10,
                                                                                    pady=10,
                                                                                    padx=15)

        # --------------------------------------------------
        row += 1
        ttk.Separator(contentFrame, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(contentFrame, text="客户还需要的资源", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)

        row += 1
        TableFrame2(contentFrame, self.Data.NeedList, clientNum, resoNum).grid(row=row,
                                                                               stick=E,
                                                                               column=0,
                                                                               columnspan=10,
                                                                               pady=10,
                                                                               padx=15)
