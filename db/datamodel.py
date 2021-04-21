from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import MetaData
import sqlalchemy as sa

Base = declarative_base()
engine = create_engine('sqlite:///kompresory.db')
metadata = MetaData()

class OlvOrder():
    """
    Book model for ObjectListView
    """
    #----------------------------------------------------------------------
    def __init__(self, order_id, operator_id, order_name, project_name, comment, operator_name):
        self.order_id = order_id  # unique row id from database
        self.operator_id = operator_id
        self.order_name = order_name
        self.project_name = project_name
        self.comment = comment
        self.operator_name = operator_name

class Operator(Base):
    __tablename__ = 'operator'
    operator_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    orders = relationship('Orders')

    def __repr__(self):
        str_out = 'operator_id={} name={}'
        str_formated = str_out.format(self.operator_id, self.name)
        return str_formated

class Orders(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    operator_id = Column(Integer, ForeignKey("operator.operator_id"), default=0)
    order_name = Column(String)
    project_name = Column(String)
    comment = Column(String, nullable=True)
    date_create = Column(DateTime, nullable=False, server_default=sa.func.now())
    progress = Column(Integer, default=0)
    order_detail = relationship('OrderDetail', back_populates='orders')

    def __repr__(self):
        str_out = 'order_id={} operator_id={} order_name={} project_name={},date_create={}, comment={}'
        str_formated = str_out.format(self.order_id, self.operator_id, self.order_name,
                                      self.project_name, self.date_create, self.comment)
        return str_formated


class OrderDetail(Base):
    __tablename__ = 'order_detail'
    order_detail_id = Column(Integer, primary_key=True, autoincrement=True)
    name_of_drowing = Column(String)
    material = Column(String)
    type_of_detail = Column(String)
    orders_id = Column(Integer, ForeignKey('orders.order_id'))
    orders = relationship("Orders", back_populates='order_detail')



Base.metadata.create_all(engine)
