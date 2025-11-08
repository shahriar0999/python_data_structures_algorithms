# from constructor import LinkedList

# my_linked_list = LinkedList(5)

# def print_list(linked_list):
#     temp = linked_list.head
#     while temp is not None:
#         print(temp.value)
#         temp = temp.next

# print_list(my_linked_list)  # Should print 5


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(5)
my_linked_list.print_list() # Should return the head node with value 5