from typing import List
from sqlalchemy.orm import Session
from db.datamodel import Operator
from repositories.IOperatorRepository import IOperatorRepository


class OperatorRepository(IOperatorRepository):

    def __init__(self, session: Session):
        self.session = session

    def find(self, operator_id: int) -> Operator:
        pass

    def find_all(self) -> List[Operator]:
        pass

    def save(self, operator: Operator) -> None:
        self.session.add(operator.name)
        self.session.commit()

    def delete(self, operator: Operator) -> None:
        pass
