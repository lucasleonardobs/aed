from node import Node


class Queue:
    def __init__(self) -> None:
        self._size: int = 0
        self.head: Node = None
        self.top: Node = None

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        result = ""

        pointer = self.head

        while pointer:
            result += f"{pointer.value} "
            pointer = pointer.next

        return result
        
    def __str__(self) -> str:
        return self.__repr__()

    def push(self, value) -> None:
        node = Node(value)

        if not self.head:
            self.top = node
            self.head = node
        else:
            self.top.next = node
            self.top = node

        self._size ++ 1

    def pop(self) -> int:
        if self.head:
            node = self.head
            self.head = self.head.next

            return node

        raise IndexError("The queue is empty")

    def peek(self) -> int:
        if self.head:
            node = self.head

            return node

        raise IndexError("The queue is empty")
