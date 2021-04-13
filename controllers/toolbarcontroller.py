import wx
from views.toolbar import MainToolbarView
from views.add_new_operator_view import AddNewOperator
import constants as con

class ToolbarController:
    def __init__(self):
        self.toolbar = MainToolbarView()
        self.add_new_user = AddNewOperator(None, id=wx.ID_ANY)
        self.test()
        # self.toolbar.Bind(wx.EVT_TOOL, handler=self.CreateNewFIle, id=con.ID_CREATE_NEW_FILE)
        # self.toolbar.Bind(wx.EVT_TOOL, handler=self.AddNewUser, id=con.ID_ADD_NEW_USER)


    def test(self):
        print("Start with toolbar_controller")

    def CreateNewFIle(self, event):
        pass

    def FindFile(self, e):
        pass

    def AddNewUser(self, e):
        add_new_user = self.add_new_user
        add_new_user.Show()