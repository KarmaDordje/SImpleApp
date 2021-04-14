import wx
import constants as con
from controllers.ToolBarController import ToolbarController

class MainToolbarView(wx.ToolBar):
    """Create tool bar."""

    def __init__(self, *args, **kwargs):
        wx.ToolBar.__init__(self, *args, **kwargs)
        self.toolbar_controller = ToolbarController()

        create_new_order_png = wx.Bitmap('icons/create.png')
        add_new_user_png = wx.Bitmap('icons/add_new_user.png')
        find_order = wx.Bitmap('icons/find.png')

        self.AddTool(con.ID_CREATE_NEW_FILE, 'Create new order', create_new_order_png)
        self.AddTool(con.ID_ADD_NEW_USER, 'Create new user', add_new_user_png)
        self.AddTool(con.ID_FIND_USER, 'Find user', find_order)
        self.SetToolShortHelp(con.ID_CREATE_NEW_FILE, 'Create new order ...')
        self.SetToolShortHelp(con.ID_ADD_NEW_USER, 'Create new user ...')
        self.SetToolShortHelp(con.ID_FIND_USER, 'Create new user ...')

        self.Realize()

        self.Bind(wx.EVT_TOOL, self.toolbar_controller.AddNewUser, id=con.ID_ADD_NEW_USER)
        self.Bind(wx.EVT_TOOL, self.toolbar_controller.CreateNewFIle, id=con.ID_CREATE_NEW_FILE)
