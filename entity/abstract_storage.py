from abc import ABC, abstractmethod
from typing import Dict


class AbstractStorage(ABC):
    def __init__(self, items: Dict[str, int], capacity: int):
        self.items = items
        self.capacity = capacity

    @abstractmethod
    def add(self, name, quantity):
        pass

    @abstractmethod
    def remove(self, name, quantity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
