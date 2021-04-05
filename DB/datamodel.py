from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import MetaData
import sqlalchemy as sa

Base = declarative_base()
engine = create_engine('sqlite:///kompresory.db')
metadata = MetaData()


class Operator(Base):
    __tablename__ = 'operator'
    operator_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    orders = relationship('Orders')


class Orders(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    opator_id = Column(Integer, ForeignKey("operator.operator_id"))
    order_name = Column(String)
    project_name = Column(String)
    comment = Column(String, nullable=True)
    # date_create = Column(DateTime, nullable=False, server_default=sa.func.now())
    order_detail = relationship('OrderDetail', back_populates='orders')


class OrderDetail(Base):
    __tablename__ = 'order_detail'
    order_detail_id = Column(Integer, primary_key=True, autoincrement=True)
    name_of_drowing = Column(String)
    material = Column(String)
    type_of_detail = Column(String)
    orders_id = Column(Integer, ForeignKey('orders.order_id'))
    orders = relationship("Orders", back_populates='order_detail')


Base.metadata.create_all(engine)
