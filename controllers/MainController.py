from views.MainView import MainWindow
from mvc_layer.Model import Model
from pubsub import pub
from db.datamodel import Operator
from controllers.AddNewOperatorController import AddNewOperatorController
from .CreateNewOrderController import CreateNewOrderController
from .OrdersTableController import OrdersTableController
from views.AddNewOperatorView import AddNewOperator
import constants as con
import wx


class ApplicationController:
    def __init__(self):
        self.main_window_view = MainWindow(parent=None)
        self.model = Model()
        self.operator = Operator()
        self.new_operator = AddNewOperatorController()
        self.order_table_controller = OrdersTableController()
        self.create_new_Order_controller = CreateNewOrderController()


    def main(self):
        self.main_window_view.main()
        print('start from controller')
