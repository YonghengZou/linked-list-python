from typing import Any, Optional
# from link_list import Node

class Node:
    
    def __init__(self, value: Any, next=None) -> None:
        self.__value = value
        self.__next = next

    def set_value(self, value: Any):
        self.__value = value
    
    def get_value(self):
        return self.__value
    
    def set_next(self, next: 'Node'):
        self.__next = next

    def get_next(self):
        return self.__next