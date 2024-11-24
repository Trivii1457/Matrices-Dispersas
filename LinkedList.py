from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    # Método para agregar un valor a la lista
    def add(self, value):
        if self.head is None: # Si la lista está vacía
            self.head = Node(value) # Se crea un nodo con el valor
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def get(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        return current.value

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __str__(self):
        return "[" + ", ".join(str(x) for x in self) + "]"