import os
from views.ToolBarView import MainToolbarView
from views.MainManuBarView import MainManuBarView
from views.AddNewOperatorView import AddNewOperator
from views.CreateNewOrderView import CreateNewOrderView
import wx
import constants as con


class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.InitUI()
        self.SetMenuBar(MainManuBarView())
        self.SetToolBar(MainToolbarView(self))
        self.add_new_view = AddNewOperator(None, id=con.ID_ADD_NEW_USER)
        self.create_new_order_view = CreateNewOrderView(None, id=con.ID_CREATE_NEW_FILE)


    def InitUI(self):
        self.SetSize(1000, 500)
        self.SetTitle('SimpleApp')
        self.Center()

    @staticmethod
    def main():
        app = wx.App()
        ex = MainWindow(parent=None)
        ex.Show()
        app.MainLoop()


#


if __name__ == '__main__':
    MainWindow.main()
