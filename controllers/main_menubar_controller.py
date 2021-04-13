import wx
from views.main_munebar_view import MainManuBarView
from views.add_new_operator_view import AddNewOperator
import constants as con


class MainMenuBarController():
    def __init__(self):
        self.menubar = MainManuBarView()
        #self.main_window = MainWindow
        self.add_new_user_view = AddNewOperator(None)
        self.echo()

        self.menubar.Bind(wx.EVT_MENU, handler=self.CreateNewFIle, id=wx.ID_ANY)
        self.menubar.Bind(wx.EVT_MENU, handler=self.SaveNewOrder, id=wx.ID_ANY)
        self.menubar.Bind(wx.EVT_MENU, handler=self.OnQuit, id=wx.ID_ANY)
        self.menubar.Bind(wx.EVT_MENU, handler=self.AddNewUser, id=wx.ID_ANY)

    def echo(self):
        print("GGGGGGGGGGGGGGGGG")

    def CreateNewFIle(self, event):
        pass

    def FindFile(self, e):
        pass

    def AddNewUser(self, e):
        add_new_user = self.add_new_user_view
        add_new_user.Show()

    def SaveNewOrder(self, e):
        pass

    def OnQuit(self, event):
        wx.EVT_CLOSE.Close()

