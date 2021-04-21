from abc import abstractmethod, ABC
from typing import List
from db.datamodel import Orders


class IOrdersRepository(ABC):

    @abstractmethod
    def find(self, order_id: int) -> Orders:
        pass

    @abstractmethod
    def find_all(self) -> List[Orders]:
        pass

    @abstractmethod
    def save(self, order: Orders) -> None:
        pass

    @abstractmethod
    def delete(self, order: Orders) -> None:
        pass
