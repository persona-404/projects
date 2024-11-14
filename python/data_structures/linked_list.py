class Node:
    def __init__(self, value=None):
        self.value = value
        self.pointer_next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node_value):
        # create new node
        new_node = Node(node_value)

        # if head is empty, then the head is now the new node
        if (self.head == None):
            self.head = new_node
        else:
            current = self.head # the cursor is always at the beginning
            while current.pointer_next_node: # if the pointer part has data
                current = current.pointer_next_node
            # here, we have traversed the "list"
            # then, whoever current eneded up to be, since it is an object, we add the new node and now it will point
                # to it. Think of a line of people pointing to each other. Each one is a person with a name and they have to point to whoever is the next one
            current.pointer_next_node = new_node

    def prepend(self, node_value):
        new_node = Node(node_value)
        new_node.pointer_next_node = self.head
        self.head = new_node

    def print(self):
        current = self.head
        while current: # at some point, it will point to null because we are assigning our "current" to whatever is in the node next_pointer
            print ("list content:", current.value)
            current = current.pointer_next_node

if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append('alylu');
    linked_list.append('joseph');
    linked_list.prepend('miles');
    linked_list.prepend('chiquita');

    linked_list.print()

        
