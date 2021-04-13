from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa
from db.datamodel import Operator, Orders, OrderDetail
from pubsub import pub

engine = sa.create_engine('sqlite:///kompresory.db')
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

'''
--------------> SECTION INSERT DATA INTO DB <----------------------
'''


def add_new_record_into_all_tables(
        operator_name,
        operator_id, order_name, project_name, comment,
        name_of_drowing, material, type_of_detail
):
    name1 = (
        session.query(Operator)
            .filter(Operator.name == operator_name)
            .one_or_none()
    )
    if name1 is not None:

        print("Alerady exist")
    else:
        name = Operator(name=operator_name)
        session.add(name)

    new_order = (
        session.query(Orders)
            .filter(Orders.opator_id == operator_id)
            .filter(Orders.order_name == order_name)
            .filter(Orders.project_name == project_name)
            .one_or_none()
    )
    if new_order is None:
        ins = Orders(opator_id=operator_id, order_name=order_name,
                     project_name=project_name, comment=comment)
        session.add(ins)

    new_order_details = (
        session.query(OrderDetail)
               .filter(OrderDetail.name_of_drowing == name_of_drowing)
               .one_or_none()
    )
    if new_order_details is None:
        ins = OrderDetail(
            name_of_drowing=name_of_drowing,
            material=material,
            type_of_detail=type_of_detail,

        )
        session.add(ins)
    session.commit()


# # test = add_new_record_into_all_tables('Poc', 1, 'ZW 666', '22 WEd', 'Test comment', '111A',
# #                                'S375', 'blacha')
# print(test)

def create_new_operator(name):
    # c1 = Operator(name=name)
    # session.add(c1)
    # session.commit()
    name1 = (
        session.query(Operator)
            .filter(Operator.name == name)
            .one_or_none()
    )
    if name1 is not None:
        pub.sendMessage('user exist', msg='User already exist')
    else:
        name = Operator(name=name)
        session.add(name)
    session.commit()
    pub.sendMessage('user exist', msg='User created successfully')


# create_new_operator('Jarek')
# exists = session.query(Operator.name).filter_by(name='Jarek').first() is not None
# print(exists)

def helper_get_operator_id():
    results = []
    with engine.connect() as connection:
        names = connection.execute(sa.select([Operator.name]))
        for row in names:
            results.append(row)
    # print(results)
    return results


def create_new_order(operator_id, order_name, project_name, comment=None):
    # operator_names = helper_get_operator_id()
    # ins = Orders(opator_id=operator_id, order_name=order_name,
    #              project_name=project_name, comment=comment)
    # session.add(ins)
    # session.commit()
    new_order = (
        session.query(Orders)
            .filter(Orders.opator_id == operator_id)
            .filter(Orders.order_name == order_name)
            .filter(Orders.project_name == project_name)
            .one_or_none()
    )
    if new_order is None:
        ins = Orders(opator_id=operator_id, order_name=order_name,
                     project_name=project_name, comment=comment)
        session.add(ins)
    session.commit()


# create_new_order(2, 'ZW 25', '654', 'Test')


def create_new_orders_detail(name_of_drowing, material, type_of_detail):
    new_order_details = (
        session.query(OrderDetail)
            .filter(OrderDetail.name_of_drowing == name_of_drowing)
            .one_or_none()
    )
    if new_order_details is None:
        ins = OrderDetail(
            name_of_drowing=name_of_drowing,
            material=material,
            type_of_detail=type_of_detail,
        )
        session.add(ins)
    session.commit()


# create_new_orders_detail('654-025-111-200', 'S355', 'Kostka')
'''
------------------> SECTION READ DATA FROM DB <----------------
'''


def get_operator(session):
    return session.query(Operator).order_by(Operator.operator_id).all()


def get_orders_by_operator(name_of_operator):
    query = session.query(
        Operator.name,
        Orders.order_name,
        Orders.project_name
    )
    join_query = query.join(Orders)
    return join_query.filter(Operator.name == name_of_operator).all()


# a = get_orders_by_operator('Piotr')
# print(a)

def get_operator_by_order(name_of_order):
    query = session.query(
        Orders.order_name,
        Operator.name
    )
    join_query = query.join(Operator)
    return join_query.filter(Orders.order_name == name_of_order).all()

# a = get_operator_by_order('ZW 666')
# print(a)
