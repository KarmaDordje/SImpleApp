from typing import List

from db.datamodel import Operator
from repositories.IOperatorRepository import IOperatorRepository


class OperatorRepository(IOperatorRepository):
    def find(self, operator_id: int) -> Operator:
        pass

    def find_all(self) -> List[Operator]:
        pass

    def save(self, operator: Operator) -> None:
        pass

    def delete(self, operator: Operator) -> None:
        pass
