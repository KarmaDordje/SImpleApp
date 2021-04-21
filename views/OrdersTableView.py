import wx
from ObjectListView import ObjectListView, ColumnDefn
from controllers.OrdersTableController import OrdersTableController
from pubsub import pub

menu_titles = [ "Open Order Detail",
                "Change Order",
                "Delete"
                ]

menu_title_by_id = {}
for title in menu_titles:
    menu_title_by_id[ wx.NewId() ] = title

class OrdersTableView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self,parent)
        self.OnInit()

    def OnInit(self):
        self.orders_controller = OrdersTableController()
        self.all_orders = self.orders_controller.get_all_orders()
        self.InitWidgets()

    def InitWidgets(self):
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        searchSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        font = wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        cat = ["Operator", "Order name", "Project name"]
        searchByLbl = wx.StaticText(self, label="Search By:")
        searchByLbl.SetFont(font)
        searchSizer.Add(searchByLbl, 0, wx.ALL, 5)
        self.categories = wx.ComboBox(self, value="Order name", choices=cat)
        searchSizer.Add(self.categories, 0, wx.ALL, 5)
        self.search = wx.SearchCtrl(self, style=wx.TE_PROCESS_ENTER)
        searchSizer.Add(self.search, 0, wx.ALL, 5)
        self.orders_list_ovl = ObjectListView(self, wx.ID_NEW, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.orders_list_ovl.SetEmptyListMsg("No Records Found")
        self.set_orders()
        addRecordBtn = wx.Button(self, label="Update table")
        addRecordBtn.Bind(wx.EVT_BUTTON, self.update)
        btnSizer.Add(addRecordBtn, 0, wx.ALL, 5)
        mainSizer.Add(searchSizer)
        mainSizer.Add(self.orders_list_ovl, 1, wx.ALL | wx.EXPAND, 10)
        mainSizer.Add(btnSizer, 0, wx.CENTER)
        self.SetSizer(mainSizer)

        self.orders_list_ovl.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.RightClick)

    menu_titles = ["Open Order Detail",
                   "Change Order",
                   "Delete"
                   ]

    menu_title_by_id = {}
    for title in menu_titles:
        menu_title_by_id[wx.NewId()] = title

    def set_orders(self):
        self.orders_list_ovl.SetColumns([
            ColumnDefn("Order ID", "left", 50, "order_id"),
            ColumnDefn("Operator ID", "left", 100, "operator_id"),
            ColumnDefn("Order Name", "left", 200, "order_name"),
            ColumnDefn("Project Name", "center", 200, "project_name"),
            ColumnDefn("Create at", "center", 200, "date_create"),
            ColumnDefn("Comment", "left", 200, "comment")

        ])
        self.set_table_list(self.all_orders)

    def set_table_list(self, data):
        self.orders_list_ovl.SetObjects(data)


    def update(self, e):
        self.show_all_orders()

    def show_all_orders(self):
        self.all_orders = self.orders_controller.get_all_orders()
        self.set_orders()

    def RightClick(self, event):
        # record what was clicked
        self.list_item_clicked = self.orders_list_ovl.GetSelectedObject()

        menu = wx.Menu()
        menu.Bind(wx.EVT_MENU, self.MenuSelectionCb)

        for (id_, title) in menu_title_by_id.items():
            ### 3. Launcher packs menu with Append. ###
            menu.Append(id_, title)

        ### 5. Launcher displays menu with call to PopupMenu, invoked on the source component, passing event's GetPoint. ###
        # self.frame.PopupMenu( menu, event.GetPoint() )
        self.PopupMenu(menu, event.GetPoint())
        menu.Destroy()  # destroy to avoid mem leak

    def MenuSelectionCb(self, event):
        # do something
        operation = menu_title_by_id[event.GetId()]
        target = self.list_item_clicked.order_id
        print('Perform "%(operation)s" on "%(target)s."' % vars())

