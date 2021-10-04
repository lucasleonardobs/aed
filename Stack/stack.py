class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Node = None


class Stack:
    def __init__(self) -> None:
        self._size: int = 0
        self.top: Node = None

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        result = ""
        pointer = self.top

        while pointer:
            result += f"{pointer.value}\n"
            pointer = pointer.next

        return result

    def __str__(self) -> str:
        return self.__repr__()

    def push(self, value) -> None:
        node = Node(value)

        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self) -> int:
        if self.top:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.value

        raise IndexError("The stack is empty")

    def peek(self) -> int:
        if self.top:
            return self.top.value

        raise IndexError("The stack is empty")
