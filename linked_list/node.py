from typing import Any


class Node:
    
    def __init__(self, value: Any = None, 
                        next: 'Node' = None) -> None:
        self.__value = value
        self._next = next

    def set_value(self, value: Any) -> None:
        self.__value = value
    
    def get_value(self) -> None:
        return self.__value
    
    def set_next(self, next: 'Node') -> None:
        self._next = next

    def get_next(self) -> None:
        return self._next
    