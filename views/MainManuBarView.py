import wx
from controllers.MainMenuController import MainMenuBarController
import constants as con
class MainManuBarView(wx.MenuBar):
    def __init__(self):
        wx.MenuBar.__init__(self)
        self.menubar_controller = MainMenuBarController()
        file_menu = wx.Menu()
        file_menu.Append(con.ID_CREATE_NEW_FILE, "&New")
        file_menu.Append(wx.ID_ANY, "&Open")
        file_menu.Append(wx.ID_ANY, "&Save")
        quit = wx.MenuItem(file_menu, con.ID_EXIT, "&Quit\tCtrl+Q")
        file_menu.Append(quit)
        self.Bind(event=wx.EVT_MENU, handler=self.menubar_controller.CreateNewFIle,
                           id=con.ID_CREATE_NEW_FILE)
        self.Append(file_menu, "&File")


