from linked_list import LinkedList, Node
# from binary_search_tree import BST, Node
from timeit import default_timer as timer
import random

q1_linked_list = LinkedList()

for i in range(10):
    Num = int(random.uniform(1,30))
    q1_linked_list.add(Node(Num))
print(q1_linked_list)

def findMaxVal(linked_list):
    MaxVal = int(0)
    for i in range(q1_linked_list.size):
        checkNum = linked_list.get(i)
        if(checkNum.data > MaxVal):
            MaxVal = q1_linked_list.get(i).data
    return MaxVal