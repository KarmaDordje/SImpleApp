from mvc_layer.Model import Model
from db.datamodel import Orders
from pubsub import pub


class CreateNewOrderController():
    def __init__(self):
        self.model = Model()
        pub.subscribe(self.AddNewRecord, 'add_new_order')


    def AddNewRecord(self, arg):
       new_order = Orders()
       new_order.order_name = arg[0]
       new_order.project_name = arg[1]
       new_order.comment = arg[2]
       self.model.create_new_order(new_order)
       print(f"controller got {arg}")



