import wx
from pubsub import pub

class AddNewOperator(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, size=(250, 150))
        wx.Frame.CenterOnScreen(self)
        self.InitUI()
        self.Centre()
        pub.subscribe(self.user_already_exist, 'user exist')


    def InitUI(self):

        panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(3, 2, 9, 25)

        title = wx.StaticText(panel, label="Add new user")
        self.status = wx.StaticText(panel, label="")

        self.tc1 = wx.TextCtrl(panel)

        btn1 = wx.Button(panel, label='Create', size=(70, 30))
        btn2 = wx.Button(panel, label='Cancal', size=(70, 30))

        fgs.AddMany([(title), (self.tc1, 1, wx.EXPAND),
                     btn1, btn2, (self.status, 1, wx.ALIGN_CENTER)])

        fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        panel.SetSizer(hbox)

        self.Bind(wx.EVT_BUTTON, self.OnCreate, btn1)
        self.Bind(wx.EVT_BUTTON, self.OnDestroy, btn2)

    def OnCreate(self, e):
        text = self.tc1.GetValue()
        pub.sendMessage('my_topic', arg=text)
        self.tc1.Clear()
        wx.MessageBox('Operator added', 'Info',
                      wx.OK | wx.ICON_INFORMATION)
        self.OnDestroy(self)
    def user_already_exist(self, msg):
        self.status.SetLabel(msg)

    def OnDestroy(self, e):
        self.Destroy()