from typing import Any
from .linked_list.link_list import LinkList
import random


def generate_link_list(objs: Any) -> LinkList:
    if len(objs)==0:
        return LinkList()
    link_list = LinkList()
    for i in objs:
        link_list.add_back(i)
    return link_list

# main file for testing linked list module
if __name__=='__main__':
    objs = random.sample(range(1, 20), 10)
    link_list = LinkList()
    link_list.add_back(1)
    link_list.add_front(2)
    link_list.insert_at(2,100)
    link_list.add_back(3)
    print(link_list)
    link_list.remove_front()
    print(link_list.get_size())
    link_list.remove_back()
    link_list.add_back(5)
    link_list.update_val(5, 100000)
    print(link_list)
    print(link_list.get_size())
    print(link_list.get_node(1))
    