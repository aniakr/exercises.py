class Node:
    def __init__(self, data=None):
        # by default data and pointer set to None - why
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        # this head is without data, it's just placeholder (list lenght = 0)

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        elements = []
        while current.next != None:
            current = current.next
            elements.append(current.data)
        print(elements)

    def lenght(self):
        current = self.head
        lenght = 0
        while current.next != None:
            current = current.next
            lenght += 1
        return lenght

    def get(self, index):
        current = self.head
        cur_index = 0
        if index >= self.lenght():
            return "Index out of range"
        while cur_index != index:
            current = current.next
            cur_index += 1
        return current.next.data


    def add_at_index(self, data, index):
        if index >= self.lenght():
            return "Index out of range"
        new_node = Node(data)
        cur_index = 0
        current = self.head
        while True:
            if cur_index == index:
                new_node.next=current.next
                current.next = new_node
                return
            current = current.next
            cur_index += 1


    def remove_at_index(self, index):
        if index >= self.lenght():
            return "Index out of range"
        cur_index = 0
        current = self.head
        while True:
            last_node = current
            current = current.next
            if cur_index == index:
                last_node.next = current.next
                return
            cur_index += 1

# stack, queue - klasy z L_lista jako pole ale z ograniczonymi metodami

