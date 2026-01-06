class Node:
    """
    an object for storing a single node of a linked list.
    models two attributes - data and the link to the next node in the list
    """
    
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
    """
    singly linked list
    """
    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        Retrun a string representation of the list
        Takes O(n) time i.e linear time
        """

        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return '-> '.join(nodes)

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        returns the number of nodes in the list
        takes O(n) time i.e linear time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        adds new Node containing data at head of the list
        takes O(1) i.e constant time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        search for the first node containing data that matches the key
        return the node or 'None' if not found
        takes O(n) time i.e linear time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        inserts a new Node containing data at index position
        insertion in singly linked lists, it takes O(1) time i.e constant time because just few references of nearby nodes are changed
        but to find the node at the given index, it takes O(n) time i.e linear time

        Takes O(n) time i.e linear time overall
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new_node = Node(data)

            position = index
            current = self.head

            while position > 1 and current:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node
            
            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, key):
        """
        removes the first occurrence of a node that contains data that matches the key
        takes O(n) time i.e linear time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current
    
    def node_at_index(self, index):
        """
        returns the node at a given index
        takes O(n) time i.e linear time
        """
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index and current:
                current = current.next_node
                position += 1

            return current