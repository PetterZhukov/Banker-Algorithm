import os
import tkinter.messagebox
from http import client
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

from Calculation_module.calculateOrder import dfs_Search
from Calculation_module.initModel import initData
from Constant.constant import transNumlistToAlplist

textlen = 7


def setTableText(master, toText, i, j, _textlen=textlen):
    # 表格中第i行j列
    # with textLen
    table = Text(master, width=_textlen, height=2)
    table.insert("end", toText)
    table.grid(row=i, column=j)


class ShowAnslist():
    def __init__(self, ansClass: dfs_Search):
        self.root = Toplevel()
        self.ansClass = ansClass
        self.root.geometry(f"{max(650,8*self.ansClass.clientNum+120)}x800")
        self.root.title("安全序列")
        # set the size

        self.creatScroAndTable()

    class ansTableFrame(Frame):
        def __init__(self, master, anslist,clientNum):
            Frame.__init__(self, master)
            self.clientNum=clientNum
            self.root = master
            self.anslist = anslist
            self.__creatTable()

        def __creatTable(self):
            titleList = [' 序号', '   释放序列', ' 用时']
            textLenList = [6,max(30,6*self.clientNum+8), 8]
            # 标题
            for j in range(3):
                setTableText(
                    self, f'{titleList[j]}',0, j, textLenList[j])
            changeSizeFun=lambda x:f"{x:>4}"
            # 内容
            for i in range(len(self.anslist)):
                setTableText(
                    self, f'{i+1:>{textLenList[0]-1}}', i+1, 0, textLenList[0])
                setTableText(
                    self, f'{"Name:":<6}{",".join(map(changeSizeFun,transNumlistToAlplist(self.anslist[i].retFinalRecord().retClientList())))}\n{"Begin:":>6}{",".join(map(changeSizeFun,self.anslist[i].retFinalRecord().retBeginTimeList()))}', i+1, 1, textLenList[1])
                setTableText(
                    self, f'{self.anslist[i].retEndTime():>{textLenList[2]-1}}', i+1, 2, textLenList[2])


    def showPage(self):
        self.root.mainloop()

    def creatScroAndTable(self):
        canvas = Canvas(master=self.root, width=800)
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
        self.creatAnsTable(contentFrame)
        # 更新Frame大小，不然没有滚动效果
        contentFrame.update()
        # 将滚动按钮绑定只Canvas上
        canvas.configure(yscrollcommand=scro.set,
                         scrollregion=canvas.bbox("all"))
        scro.config(command=canvas.yview)

    def creatAnsTable(self, contentFrame):

        row = 0
        Label(contentFrame).grid(row=row)

        row += 1
        Label(contentFrame, text="安全序列",
              font=('宋体', 20, 'bold'))\
            .grid(row=row, column=0, columnspan=4)

        # --------------------------------------------------
        row += 1
        ttk.Separator(contentFrame, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        # 当前安全序列
        Label(contentFrame, text="求出的安全序列数:", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)

        ansNum = StringVar()
        ansNum.set(str(self.ansClass.retAnsNum()))
        ansNumEntry = Entry(contentFrame, textvariable=ansNum,state='disable').grid(row=row, column=1, sticky=W)
        
        row += 1
        # 最少时间
        Label(contentFrame, text="最短用时:", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)

        leastTime = StringVar()
        leastTime.set(self.ansClass.retMinTimeAns().retEndTime())
        leastTimeEntry = Entry(contentFrame, textvariable=leastTime,state='disable').grid(row=row, column=1, sticky=W)
        

        # --------------------------------------------------
        row += 1
        ttk.Separator(contentFrame, orient='horizontal').grid(
            row=row, column=0, rowspan=1, columnspan=4, sticky='EW', pady=5, padx=5)

        row += 1
        Label(contentFrame, text="安全序列显示", font=('宋体', 13, 'bold')).grid(
            row=row, sticky=E, padx=35)

        self.ansTableFrame(contentFrame, self.ansClass.retAnsList(),self.ansClass.clientNum).grid(row=row,
                                                                  stick=E,
                                                                  column=0,
                                                                  columnspan=10,
                                                                  pady=10,
                                                                  padx=15)
