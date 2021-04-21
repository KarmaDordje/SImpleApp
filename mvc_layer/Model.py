from repositories.OperatorRepository import OperatorRepository
from repositories.OrdersRepository import OrdersRepository
from db.datamodel import Operator, Orders
from sqlalchemy.orm import Session

class Model:
    def __init__(self):
        self.session = Session()
        self.operator_repo = OperatorRepository(self.session)
        self.orders_repo =OrdersRepository(self.session)
        self.operator = Operator()
        self.order = Orders()



    def add_new_user(self, operator:Operator):
        self.operator_repo.save(operator)

    def get_all_orders(self):
        self.orders_repo.find_all()

    def get_orders_by_operator(self):
        orders = self.orders_repo.get_orders_by_operator()
        return orders

    def create_new_order(self, order:Orders):
        self.orders_repo.save(order)
