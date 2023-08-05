from linked_list import LinkedList, Node
from timeit import default_timer as timer
import random
import color

def main():
    print("\nLinked List driver!\n")

    my_linked_list = LinkedList() # creates an empty linked list, size 0, and head points to None
    my_python_list = [] # created an empty python list

    listLen = int(10000) # var to change the list size

    divider()
    print(f"Adding {listLen} numbers in a Python List... ")

    start = timer()
    for i in range(listLen): # inserting 10,000 random number in the python list
        randomNum = random.uniform(1,1000000)
        my_python_list.append(randomNum)
    end = timer()

    print(f"Time to add {len(my_python_list)} numbers in a Python List: {end - start} seconds\n") # time it took to insert the number in the python list
    divider()

    print(f"Adding the same {listLen} Numbers in a Linked List...")

    start = timer()
    for i in range(len(my_python_list)): # inserting the numbers from the python list into the linked list
        Num = my_python_list[i]
        my_linked_list.add(Node(Num))
    end = timer()

    print(f"Time to add {my_linked_list.size} numbers in a Linked List: {end - start} seconds\n")  # Time in seconds, e.g. 5.38091952400282
    divider()

    # analysis of time and steps for number insertion into a linked list vs. a python list
    print(f'{color.CYAN}For a Linked List, the number of steps to add an object increase exponentially\
          \nas the size of the linked list grows. For example, to add the 10,000th object\
          \nin a linked list full of 9,999 object, it will take 9,999 steps to iterate\
          \nthrough the list and get to the end of it first, before you could add the new object.{color.END}\n')
    divider()
    
    print('Getting the 10th number from the Linked List...')

    start = timer()
    Num10 = my_linked_list.get(10) # get the 10th number from the linked list and measure the time it took
    end = timer()
    print(f"Time to get 10th number in Linked List: {end-start} seconds\n")

    start = timer()
    Num10_Array = my_python_list[9] # get the 10th number from the python list and measure the time it took
    end = timer()
    print(f"Time to get 10th number in Python List: {end-start} seconds\n")

    # analysis of time and steps it took to retrieve the 10th number in both lists
    print(f'{color.CYAN}It takes 11 steps to find the 10th number in the Linked List because\
          \nthe list first has to iterate through all the nodes to get to the\
          \n10th one. Once the list is there, then it can look up the data at\
          \nthe 10th node and print it out. Whereas, with an array this operation\
          \nis very fast because it knows where the 10th number is stored already.{color.END}\n')   
    divider()

    print('Calculating time and steps to find 7000th number in Linked List and Array...\n')

    start = timer()
    Num7000 = my_linked_list.get(7000)
    end = timer()
    print(f"Time to get 7000th number in Linked List: {end-start} seconds\n")

    start = timer()
    Num7000_Array = my_python_list[6999]
    end = timer()
    print(f"Time to get 7000th number in Python List; {end-start} seconds\n")

    # analysis of time and steps it took to retrieve the 7000th number from both lists
    print(f'{color.CYAN}The Linked List has to iterate through the entire list to get to the 7000th\
          \nnode so it can check the data at that node, hence, the 7001 steps to get the 7000th number.\
          \nWhereas, the array takes significantly slower time since it already knows exactly where the\
          \n7000th number is stored. Therefore, it is equivalent to 1 step for the array to extract the\
          \n7000th value. The time for linked list to get a number farther in the data structure is going\
          \nto keep on increasing, however, the time for lists to do the same with always be\
          \nalmost intentaneous.{color.END}\n')
    divider()

def divider():
    print('=================================================================\n')

if __name__ == "__main__":
    main()
