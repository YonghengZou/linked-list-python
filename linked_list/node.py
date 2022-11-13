from typing import Any, Optional
# from link_list import Node

class Node:
    
    def __init__(self, value: Any = None, 
                        next: 'Node' = None) -> None:
        self.__value = value
        self._next = next

    def set_value(self, value: Any):
        self.__value = value
    
    def get_value(self):
        return self.__value
    
    def set_next(self, next: 'Node'):
        self._next = next

    def get_next(self):
        return self._next
    