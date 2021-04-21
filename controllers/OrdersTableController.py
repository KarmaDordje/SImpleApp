from db.datamodel import Orders
from mvc_layer.Model import Model


class OrdersTableController:
    def __init__(self):
        self.model = Model()



    def convertResults(self, results):
        """
        Convert results to OlvBook objects
        """
        all_orders = []
        for record in results:
            order = Orders(
                             order_id=record.order_id,
                             operator_id=record.operator_id,
                             order_name=record.order_name,
                             project_name=record.project_name,
                             comment=record.comment,
                             date_create=record.date_create

                             )
            all_orders.append(order)

        return all_orders



    def get_all_orders(self):
        #results = self.model.orders_repo.get_orders_by_operator()
        results = self.model.orders_repo.find_all()
        all_orders = self.convertResults(results)

        return all_orders

    def updete(self, e):
        self.get_all_orders()


    def test(self):
        print("Its work")