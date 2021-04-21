from typing import List
from sqlalchemy.orm import Session, sessionmaker
from db.datamodel import Operator
from repositories.IOperatorRepository import IOperatorRepository
from sqlalchemy import create_engine
from pubsub import pub
engine = create_engine('sqlite:///kompresory.db')
Session = sessionmaker(engine)


class OperatorRepository(IOperatorRepository):

    def __init__(self, session: Session):
        self.session = session
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = Session()

    def find(self, operator_id: int) -> Operator:
        find_operator = self.session.query(Operator).filter(Operator.operator_id==operator_id).fist()
        return find_operator

    def find_all(self) -> List[Operator]:
        find_all = self.session.query(Operator).all()
        return find_all

    def save(self, operator: Operator) -> None:
        self.session.add(operator)
        self.session.commit()
        pub.sendMessage('user exist', msg='User created successfully')
        self.session.close()

    def delete(self, operator: Operator) -> None:
        self.session.delete(operator)
        self.session.commit()
        self.session.close()
