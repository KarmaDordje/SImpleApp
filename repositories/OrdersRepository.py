from typing import List
from sqlalchemy.orm import Session, sessionmaker
from db.datamodel import Orders, Operator, OlvOrder
from repositories.IOrdersRepository import IOrdersRepository
from sqlalchemy import create_engine
from pubsub import pub
engine = create_engine('sqlite:///kompresory.db')
Session = sessionmaker(engine)

class OrdersRepository(IOrdersRepository):
    def __init__(self, session: Session):
        self.session = session
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = Session()

    def find(self, order_id: int) -> Orders:
        find_operator = self.session.query(Orders).filter(Orders.order_id == order_id).fist()
        return find_operator


    def find_all(self) -> List[Orders]:
        find_all = self.session.query(Orders).all()
        return find_all


    def save(self, order: Orders) -> None:
        self.session.add(order)
        self.session.commit()
        self.session.expunge_all()
        self.session.close()


    def delete(self, order: Orders) -> None:
        self.session.delete(order)
        self.session.commit()
        self.session.close()

    def get_orders_by_operator(self) -> [OlvOrder]:
        orders = self.session.query(
            Orders,
            Operator.name)
        operator = orders.join(Operator)
        return operator.filter(Orders.operator_id == Operator.operator_id).all()