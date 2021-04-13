import wx

class CreateNewOrderView(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, size=(1000, 440))
        wx.Frame.CenterOnScreen(self)

        self.InitUI()
        self.Centre()

    def InitUI(self):
        panel = wx.Panel(self)
        '''
        # ---------------> WINDOW FIELDS <----------------
        '''

        vbox = wx.BoxSizer(wx.VERTICAL)
        # hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(9, 2, 9, 20)

        order_number = wx.StaticText(panel, label='Numer zamówienia')
        name_of_project = wx.StaticText(panel, label='Nazwa projektu')
        name_of_drowing = wx.StaticText(panel, label='Numer rysunku')
        index_of_material = wx.StaticText(panel, label='Index materialu')
        typy_of_detal = wx.StaticText(panel, label='Typ wyrobu')
        comments = wx.StaticText(panel, label='Uwagi')
        date_of_adding_recort = wx.StaticText(panel, label='Data opracowania')
        name_of_operator = wx.StaticText(panel, label='Operator opracował')

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel)
        tc4 = wx.TextCtrl(panel)
        tc5 = wx.TextCtrl(panel)
        tc6 = wx.TextCtrl(panel)
        tc7 = wx.TextCtrl(panel)
        tc8 = wx.TextCtrl(panel)

        fgs.AddMany([order_number, (tc4, 1, wx.EXPAND),
                     name_of_project, (tc1, 1, wx.EXPAND),
                     name_of_drowing, (tc2, 1, wx.EXPAND),
                     index_of_material, (tc3, 1, wx.EXPAND),
                     typy_of_detal, (tc5, 1, wx.EXPAND),
                     comments, (tc6, 1, wx.EXPAND),
                     date_of_adding_recort, (tc7, 1, wx.EXPAND),
                     name_of_operator, (tc8, 1, wx.EXPAND),

                     ])

        fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)
        vbox.Add(fgs, proportion=2, flag=wx.ALL | wx.EXPAND, border=15)

        '''
        # -------------------> BUTTONS <----------------
        '''

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        create_new_record_button = wx.Button(panel, label='Create', size=(70, 30))
        hbox5.Add(create_new_record_button)
        cancel_button = wx.Button(panel, label='Close', size=(70, 30))
        hbox5.Add(cancel_button, flag=wx.LEFT | wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        panel.SetSizer(vbox)

        '''
        # ------------> BINDING <------------------
        '''

        # self.Bind(wx.EVT_BUTTON, create_new_record_button, self.AddNewRecord, id=ID_CREATE_NEW_RECORD)
        # self.Bind(wx.EVT_BUTTON, self.OnDestroyNewWindow, cancel_button, id=ID_DESTROY_WINDOW)

    def AddNewRecord(self):
        pass

    def OnDestroyNewWindow(self, e):
        self.Destroy()