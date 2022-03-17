from tkinter import *
from UI.view_OriginFrame import *
from UI.view_ReadFrame import *


class MainPage:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry('600x550+500+240')

        self.page = Frame(self.root)
        self.page.pack()
        self.__initPage()
        self.__creatMenu()
        
        self.openPage(self.OriginPage)

    def __creatMenu(self):
        menubar = Menu(self.root)
        menubar.add_command(
            label="起始页", command=lambda: self.openPage(self.OriginPage))
        menubar.add_command(
            label="打开文件", command=lambda: self.openPage(self.ReadPage))

        menubar.add_command(label="Quit", command=self.root.quit)
        self.root['menu'] = menubar

    def __initPage(self):
        self.OriginPage = OriginFrame(self.root)
        self.ReadPage = ReadFrame(self.root)

    def openPage(self, page):
        self.page.pack_forget()
        self.page = page
        self.page.pack()






