import wx
import constants as con

from pubsub import pub


class CreateNewOrderView(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, size=(500, 440))
        wx.Frame.CenterOnScreen(self)


        self.InitUI()
        self.Centre()

    def InitUI(self):
        panel = wx.Panel(self)
        '''
        # ---------------> WINDOW FIELDS <----------------
        '''

        vbox = wx.BoxSizer(wx.VERTICAL)
        fgs = wx.FlexGridSizer(9, 2, 9, 20)

        order_number = wx.StaticText(panel, label='Numer zamówienia')
        name_of_project = wx.StaticText(panel, label='Nazwa projektu')
        comments = wx.StaticText(panel, label='Uwagi')
        self.tc1 = wx.TextCtrl(panel)

        self.tc4 = wx.TextCtrl(panel)

        self.tc6 = wx.TextCtrl(panel)


        fgs.AddMany([order_number, (self.tc4, 1, wx.EXPAND),
                     name_of_project, (self.tc1, 1, wx.EXPAND),
                     comments, (self.tc6, 1, wx.EXPAND),
                     ])

        fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)
        vbox.Add(fgs, proportion=2, flag=wx.ALL | wx.EXPAND, border=15)

        '''
        # -------------------> BUTTONS <----------------
        '''

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        create_new_record_button = wx.Button(panel, con.ID_CREATE_NEW_FILE, label='Create', size=(70, 30))
        hbox5.Add(create_new_record_button)
        cancel_button = wx.Button(panel, wx.ID_CLOSE, label='Close', size=(70, 30))
        hbox5.Add(cancel_button, flag=wx.LEFT | wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        panel.SetSizer(vbox)

        '''
        # ------------> BINDING <------------------
        '''

        self.Bind(wx.EVT_BUTTON, self.AddNewRecord, create_new_record_button)
        self.Bind(wx.EVT_BUTTON, self.OnDestroyNewWindow, cancel_button)

    def OnDestroyNewWindow(self, e):
        self.Destroy()

    def AddNewRecord(self, e):
        new_order = []
        for x in (self.tc1.GetValue(), self.tc4.GetValue(), self.tc6.GetValue()):
            new_order.append(x)
        pub.sendMessage("add_new_order", arg=new_order)
        self.tc1.Clear()
        self.tc6.Clear()
        self.tc4.Clear()
        wx.MessageBox('New Order Added', 'Info',
                      wx.OK | wx.ICON_INFORMATION)
        self.OnDestroyNewWindow(self)