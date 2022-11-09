from node import Node
from list_interface import ListInterface

class LinkList(ListInterface):
    def __init__(self, head: Node = None, tail: Node = None) -> None:
        self.__head = head
        self.__tail = tail

    def add_front(self, val):
        node = Node(val)
        if self.__head==None:
            self.__head=node
            return

        node.set_next(self.__head)
        self.__head = node

    def add_back(self, val):
        node = Node(val)
        if self.__tail==None:
            self.__head=node
            self.__tail=node
            return
        self.__tail.set_next(node)
        self.__tail = node
        
    
    def __str__(self) -> None:
        cur = self.__head
        rpr = "Linked list: "
        while cur is not None:
            rpr += str(cur.get_value())+" -> "
            cur = cur.get_next()
        rpr += "None"

        return rpr