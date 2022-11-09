from typing import Any
from link_list import LinkList
import random

def generate_link_list(objs: Any) -> LinkList:
    if len(objs)==0:
        return LinkList()
    link_list = LinkList()
    for i in objs:
        link_list.add_back(i)
    return link_list

if __name__=='__main__':
    objs = random.sample(range(1, 20), 10)
    # # objs = []
    link_list = generate_link_list(objs=objs)
    # link_list = LinkList()
    # print(link_list)
    # link_list.add_back(10)
    # link_list.add_back(9)
    # link_list.add_back(8)
    # link_list.add_back(7)
    # link_list.add_back(100)
    # link_list.add_front(10000)
    # link_list.add_front('ccc')
    # link_list.add_back('ssss')

    print(link_list)
    # link_list.add_front(10)
    # print(link_list)
    