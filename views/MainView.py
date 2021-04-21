import os
from . ToolBarView import MainToolbarView
from . MainManuBarView import MainManuBarView
from . AddNewOperatorView import AddNewOperator
from . CreateNewOrderView import CreateNewOrderView
from . OrdersTableView import OrdersTableView
import wx
import constants as con


class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.InitUI()
        self.SetMenuBar(MainManuBarView())
        self.SetToolBar(MainToolbarView(self))
        self.add_new_view = AddNewOperator(self, id=con.ID_ADD_NEW_USER)
        self.create_new_order_view = CreateNewOrderView(self, id=con.ID_CREATE_NEW_FILE)
        self.orders_table_view = OrdersTableView(self)
        self.Bind(wx.EVT_CLOSE, self.on_quit_click)


    def InitUI(self):
        self.SetSize(1000, 500)
        self.SetTitle('SimpleApp')
        self.Center()

    def on_quit_click(self, event):
        """Handle close event."""
        del event
        wx.CallAfter(self.Destroy)

    @staticmethod
    def main():
        app = wx.App()
        ex = MainWindow(parent=None)
        ex.Show()
        app.MainLoop()


#


if __name__ == '__main__':
    MainWindow.main()
