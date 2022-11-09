from node import Node

class LinkList:
    def __init__(self, head: Node) -> None:
        self.__head = head
    
    def print_link_list(self):
        cur = self.__head

        while cur is not None:
            print(cur.get_value(),"->",end=' ')
            cur = cur.get_next()
        print(None)