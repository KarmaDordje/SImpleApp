from abc import abstractmethod, ABC
from typing import List

from db.datamodel import Operator


class IOperatorRepository(ABC):

    @abstractmethod
    def find(self, operator_id: int) -> Operator:
        pass

    @abstractmethod
    def find_all(self) -> List[Operator]:
        pass

    @abstractmethod
    def save(self, operator: Operator) -> None:
        pass

    @abstractmethod
    def delete(self, operator: Operator) -> None:
        pass
