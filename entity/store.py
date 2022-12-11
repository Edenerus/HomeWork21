from typing import Dict

from entity.base_storage import BaseStorage


class Storage(BaseStorage):
    def __init__(self, items: Dict[str, int], capacity=100):
        super().__init__(items, capacity)