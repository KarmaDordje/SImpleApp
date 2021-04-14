import wx
from views.AddNewOperatorView import AddNewOperator
from views.CreateNewOrderView import CreateNewOrderView
import constants as con


class MainMenuBarController():
    def __init__(self):
        self.add_new_user_view = AddNewOperator(None, id=wx.ID_ANY)


    def test(self):
        print("Meny new")

    def CreateNewFIle(self, event):
        title = 'Create new record'
        create_window = CreateNewOrderView(parent=None, id=con.ID_CREATE_NEW_FILE)
        create_window.Show()

    def FindFile(self, e):
        pass


    def SaveNewOrder(self, e):
        pass

    def OnQuit(self, event):
        wx.EVT_CLOSE.Close()

