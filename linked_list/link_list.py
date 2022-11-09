from node import Node
from list_interface import ListInterface
class LinkList(ListInterface):
    def __init__(self, head: Node) -> None:
        self.__head = head
    
    def __str__(self) -> None:
        cur = self.__head
        rpr = "Linked list: "
        while cur is not None:
            rpr += str(cur.get_value())+" -> "
            cur = cur.get_next()
        rpr += "None"

        return rpr