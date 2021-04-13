import wx
class MainManuBarView(wx.MenuBar):
    def __init__(self):
        wx.MenuBar.__init__(self)
        file_menu = wx.Menu()
        file_menu.Append(wx.ID_ANY, "&New")
        file_menu.Append(wx.ID_ANY, "&Open")
        file_menu.Append(wx.ID_ANY, "&Save")
        quit = wx.MenuItem(file_menu, wx.ID_EXIT, "&Quit\tCtrl+Q")
        file_menu.Append(quit)
        self.Append(file_menu, "&File")
