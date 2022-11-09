from typing import Any
from node import Node
from link_list import LinkList
import random

def generate_link_list(objs: Any) -> LinkList:
    nodes = list(map(Node, objs))
    for i in range(len(nodes)-1):
        nodes[i].set_next(nodes[i+1])
    return LinkList(nodes[0])

if __name__=='__main__':
    objs = random.sample(range(1, 20), 10)
    link_list = generate_link_list(objs=objs)
    print(link_list)
    