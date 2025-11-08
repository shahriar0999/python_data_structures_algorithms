from constructor import LinkedList

my_linked_list = LinkedList(5)

def print_list(linked_list):
    temp = linked_list.head
    while temp is not None:
        print(temp.value)
        temp = temp.next

print_list(my_linked_list)  # Should print 5