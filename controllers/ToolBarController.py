import wx
from views.CreateNewOrderView import CreateNewOrderView
from views.AddNewOperatorView import AddNewOperator
from views.OrdersTableView import OrdersTableView
import constants as con


class ToolbarController:
    def __init__(self):
        self.add_new_user = AddNewOperator(None, id=wx.ID_ANY)

    def test(self, e):
        print("Start with toolbar_controller")

    def CreateNewFIle(self, event):
        title = 'Create new record'
        create_window = CreateNewOrderView(parent=None, id=con.ID_CREATE_NEW_FILE)
        create_window.Show()

    def FindFile(self, e):
        table_view = OrdersTableView(parent=None)
        table_view.Show()

    def AddNewUser(self, e):
        add_new_user = AddNewOperator(None, id=con.ID_ADD_NEW_USER)
        add_new_user.Show()

