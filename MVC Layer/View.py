import wx
from pubsub import pub

ID_EXIT = 100
ID_CREATE_NEW_FILE = 200
ID_CREATE_NEW_RECORD = 300
ID_DESTROY_WINDOW = 400
ID_ADD_NEW_USER = 500
PROGECT_PATH = '/home/saszka/PycharmProjects/SimpleApp/'



class MainWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, size=(600, 400))
        self.InitUI()

    def InitUI(self):

        """
        ----------->Menu Bar <----------------
        """
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileMenu.Append(ID_CREATE_NEW_FILE, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        qmi = wx.MenuItem(fileMenu, ID_EXIT, '&Quit\tCtrl+Q')
        fileMenu.Append(qmi)

        '''
           ------------> TOOL BAR <--------------------

        '''

        toolbar = self.CreateToolBar()
        createTool = toolbar.AddTool(ID_CREATE_NEW_FILE, 'Create', wx.Bitmap(PROGECT_PATH+'/icons/create.png'))
        findToll = toolbar.AddTool(wx.ID_ANY, 'Find', wx.Bitmap(PROGECT_PATH+'/icons/find.png'))
        addNewUserToll = toolbar.AddTool(ID_ADD_NEW_USER, 'Create', wx.Bitmap(PROGECT_PATH+'/icons/add_new_user.png'))
        toolbar.Realize()

        '''
        # -----------> BINDING <-----------------------
        '''


        self.Bind(wx.EVT_TOOL, self.CreateNewFIle, createTool, id=ID_CREATE_NEW_FILE)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi, id=ID_EXIT)
        self.Bind(wx.EVT_MENU, self.CreateNewFIle, createTool, id=ID_CREATE_NEW_FILE)
        self.Bind(wx.EVT_TOOL, self.FindFile, findToll)
        self.Bind(wx.EVT_TOOL, self.AddNewUser, addNewUserToll, id=ID_ADD_NEW_USER)
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.SetSize(1000, 500)
        self.SetTitle('SimpleApp')
        self.Center()

        '''
        ---------------> F-U-N-C-T-I-O-N-S <-------------------
        '''

    def OnQuit(self, event):
        self.Close()

    def CreateNewFIle(self, event):
        title = 'Create new record'
        create_window = CreateNewRecord(parent=None)#, id=ID_CREATE_NEW_FILE)
        create_window.Show()

    def FindFile(self, e):
        pass

    def AddNewUser(self, e):
        add_new_user = AddNewOperator(parent=None)
        add_new_user.Show()
    @staticmethod
    def main():
        app = wx.App()
        ex = MainWindow(parent=None)
        ex.Show()
        app.MainLoop()


class CreateNewRecord(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, size=(1000, 440))
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
        self.Bind(wx.EVT_BUTTON, self.OnDestroyNewWindow, cancel_button, id=ID_DESTROY_WINDOW)

    def AddNewRecord(self):
        pass

    def OnDestroyNewWindow(self, e):
        self.Destroy()

class AddNewOperator(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, size=(250, 150))
        wx.Frame.CenterOnScreen(self)
        #self.controller = controller
        self.InitUI()
        self.Centre()
        pub.subscribe(self.user_already_exist, 'user exist')


    def InitUI(self):

        # self.panel = wx.Panel(self)
        # vbox = wx.BoxSizer(wx.VERTICAL)
        # hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # st1 = wx.StaticText(self.panel, label='New user name')
        # hbox1.Add(st1, flag=wx.EXPAND, border=10)
        # vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        #
        # vbox.Add(-1, 10)
        # hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        # self.tc = wx.TextCtrl(self.panel)
        # hbox3.Add(self.tc, flag=wx.EXPAND, proportion=1)
        # vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        #
        # vbox.Add(-2, 10)
        # hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        # btn1 = wx.Button(self.panel, label='Create', size=(70, 30))
        # hbox2.Add(btn1)
        # btn2 = wx.Button(self.panel, label='Cancal', size=(70,30))
        # hbox2.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        # vbox.Add(hbox2, flag=wx.ALIGN_CENTER|wx.RIGHT, border=10)
        # self.panel.SetSizer(vbox)

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

        self.Bind(wx.EVT_BUTTON, self.OnCreate, btn1, id=ID_ADD_NEW_USER)
        self.Bind(wx.EVT_BUTTON, self.OnDestroyAddNewUser, btn2,id=ID_DESTROY_WINDOW)


    def OnCreate(self, e):
        text = self.tc1.GetValue()

        pub.sendMessage('my_topic', arg=text)

    def user_already_exist(self, msg):
        self.status.SetLabel(msg)




    def OnDestroyAddNewUser(self, e):
        self.Close()

if __name__ == '__main__':
    MainWindow.main()
