from typing import Any
from .node import Node
from .list_interface import ListInterface
from ..exceptions.exceptions import EmptyException, IndexOutOfBound


class LinkList(ListInterface):
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__size = 0

    def get_node(self, index: int) -> Node:
        if self.is_empty():
            raise EmptyException("emp")
        if index>self.get_size()-1:
            raise IndexOutOfBound("index bigger than max_index of the linklist")
        cur = self.__head

        while (index):
            cur = cur._next
            index -= 1
        return cur.get_value()

    def add_front(self, val: Any) -> None:
        node = Node(val)
        if self.__head==None:
            self.__head=node
            self.__tail=node
            self.__size += 1
            return

        node._next = self.__head
        self.__head = node
        self.__size += 1

    def add_back(self, val):
        node = Node(val)
        if self.__tail==None:
            self.__head=node
            self.__tail=node
            self.__size += 1
            return
        self.__tail._next = node
        self.__tail = node
        self.__size += 1
    
    def insert_at(self, index: int, value: Any) -> None:
        if index==0:
            self.add_front(value)
        elif index>=self.get_size():
            self.add_back(value)
        else:
            cur = self.__head
            while(index-1):
                cur = cur._next
                index -= 1
            node = Node(value)
            node._next = cur._next
            cur._next = node
            self.__size += 1
    
    def remove_front(self) -> Any:
        if self.get_size()==0:
            raise EmptyException("Empty")
        if self.__size==1:
            temp = self.__head.get_value()
            self.__head = None
            self.__tail = None
            self.__size -= 1
            return temp
        temp = self.__head.get_value()
        self.__head = self.__head._next
        self.__size -= 1
        return temp
    
    def remove_back(self) -> Any:
        if self.get_size()==0:
            raise EmptyException("Empty")
        if self.__size==1:
            temp = self.__head.get_value()
            self.__head = None
            self.__tail = None
            self.__size -= 1
            return temp
        temp = self.__head.get_value()
        cur = self.__head
        while cur._next!=self.__tail:
            cur = cur._next
        cur._next = None
        self.__tail = cur
        self.__size -= 1
        return temp
    
    def update_val(self, old_val: Any, new_val: Any) -> None:
        cur = self.__head

        while(cur):
            if cur.get_value()==old_val:
                cur.set_value(new_val)
            cur=cur._next

    def get_size(self) -> int:
        return self.__size
        
    def is_empty(self) -> bool:
        return self.get_size() == 0

    def __str__(self) -> str:
        cur = self.__head
        rpr = "Linked list: "
        while cur is not None:
            rpr += str(cur.get_value())+" -> "
            cur = cur.get_next()
        rpr += "None"

        return rpr