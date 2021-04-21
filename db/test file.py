import wx

import sys
sys.path.append("..")

from ObjectListView import ObjectListView, ColumnDefn

### 2. Launcher creates wxMenu. ###
menu_titles = [ "Open",
                "Properties",
                "Rename",
                "Delete" ]

menu_title_by_id = {}
for title in menu_titles:
    menu_title_by_id[ wx.NewId() ] = title

class Track(object):
    """
    Simple minded object that represents a song in a music library
    """
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album

def GetTracks():
    """
    Return a collection of tracks
    """
    return [
        Track("Sweet Lullaby", "Deep Forest", "Deep Forest"),
        Track("Losing My Religion", "U2", "Out of Time"),
        Track("En el Pais de la Libertad", "Leon Gieco", "Leon Gieco"),
    ]

class MyFrame(wx.Frame):

    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)

        self.Init()

    def Init(self):
        self.InitModel()
        self.InitWidgets()
        self.InitObjectListView()

    def InitModel(self):
        self.songs = GetTracks()

    def InitWidgets(self):
        panel = wx.Panel(self, -1)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(panel, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(sizer_1)

        self.myOlv = ObjectListView(panel, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.myOlv, 1, wx.ALL | wx.EXPAND, 4)
        panel.SetSizer(sizer_2)

        self.Layout()

    def InitObjectListView(self):
        self.myOlv.SetColumns([
            ColumnDefn("Title", "left", 120, "title"),
            ColumnDefn("Artist", "left", 100, "artist"),
            ColumnDefn("Album", "left", 100, "album")
        ])
        self.myOlv.SetObjects(self.songs)

        self.myOlv.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightClick)

    def RightClick(self, event):
        # record what was clicked
        self.list_item_clicked = self.myOlv.GetSelectedObject()

        menu = wx.Menu()
        menu.Bind(wx.EVT_MENU, self.MenuSelectionCb)

        for (id_, title) in menu_title_by_id.items():
            ### 3. Launcher packs menu with Append. ###
            menu.Append(id_, title)

        ### 5. Launcher displays menu with call to PopupMenu, invoked on the source component, passing event's GetPoint. ###
        # self.frame.PopupMenu( menu, event.GetPoint() )
        frame_1.PopupMenu(menu, event.GetPoint())
        menu.Destroy()  # destroy to avoid mem leak

    def MenuSelectionCb(self, event):
        # do something
        operation = menu_title_by_id[ event.GetId() ]
        target = self.list_item_clicked.title
        print( 'Perform "%(operation)s" on "%(target)s."' % vars())


class MyPopupMenu(wx.Menu):

    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()

        self.parent = parent

        mmi = wx.MenuItem(self, wx.NewId(), 'Minimize')
        self.AppendItem(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)

        cmi = wx.MenuItem(self, wx.NewId(), 'Close')
        self.AppendItem(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)


    def OnMinimize(self, e):
        self.parent.Iconize()

    def OnClose(self, e):
        self.parent.Close()


if __name__ == '__main__':
    app = wx.App(False)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "ObjectListView Track Test")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()