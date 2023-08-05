from binary_search_tree import BST, Node
from timeit import default_timer as timer
import random

class Student:
    def __init__(self, id, name, major, gpa):
        self.id = id
        self.name = name
        self.major = major
        self.gpa = gpa

    def __str__(self):
        message = f"Name:{self.name}, id:{self.id}"
        return message

def main():
    print("BST driver!")

    NumberList = []
    randomNumbers = BST()

    for x in range(10000): # inserting 10,000 random number in the python list
        randomNum = int(random.uniform(1,1000000))
        NumberList.append(randomNum)

    print("Adding 10,000 random numbers to the Binary Search Tree using non recursive insertion...")

    start = timer()
    for i in range(10000):
        tmpNum = NumberList[i]
        randomNumbers.add(tmpNum,tmpNum)
    end = timer()

    print(f"Time to add all numbers to tree was {end-start} seconds")

    findNum = NumberList[100]

    start = timer()
    randomNumbers.find(findNum)
    end = timer()

    print(f"Time to find number {findNum} in the tree was {end-start} seconds")

    findNum = NumberList[7000]

    start = timer()
    randomNumbers.find(findNum)
    end = timer()

    print(f"Time to find number {findNum} in the tree was {end-start} seconds")

    print("\n=========================================================\n")

    print("Adding 10,000 random numbers to the Binary Search Tree using recursive insertion...")

    recursiveTree = BST()

    start = timer()
    for i in range(10000):
        tmpNum = NumberList[i]
        recursiveTree.recursiveAdd(tmpNum)
    end = timer()

    print(f"Time to add all numbers to tree was {end-start} seconds")

    findNum = NumberList[100]

    start = timer()
    recursiveTree.find(findNum)
    end = timer()

    print(f"Time to find number {findNum} in the tree was {end-start} seconds")

    findNum = NumberList[7000]

    start = timer()
    recursiveTree.find(findNum)
    end = timer()

    print(f"Time to find number {findNum} in the tree was {end-start} seconds")




if __name__ == "__main__":
    main()
