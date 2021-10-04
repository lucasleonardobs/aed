class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Node = None


class LinkedList:
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

    def _getnode(self, index: int) -> Node:
        i = 0
        pointer = self.head

        while pointer:
            if i == index:
                return pointer

            pointer = pointer.next
            i += 1

        raise IndexError("Index out of range")

    def __getitem__(self, index: int) -> int:
        return self._getnode(index).value

    def __setitem__(self, index: int, value: int) -> None:
        if index > self._size:
            raise IndexError("Index out of range")

        pointer = self._getnode(index)
        pointer.value = value

    def push(self, value: int) -> None:
        if self.head:
            self.top.next = Node(value)
            self.top = self.top.next
        else:
            node = Node(value)
            self.head = node
            self.top = node

        self._size += 1

    def insert(self, index: int, value: int) -> None:
        node = Node(value)

        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node.next = pointer.next
            pointer.next = node

        self._size += 1

    def remove(self, value) -> None:
        if self.head and self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next

            while pointer:
                if pointer.value == value:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size -= 1

                    return True

                ancestor = pointer
                pointer = pointer.next

        raise ValueError(f"{value} is not in list")

    def index(self, value: int) -> int:
        i = 0
        pointer = self.head

        while pointer:
            if pointer.value == value:
                return i

            pointer = pointer.next
            i += 1

        raise ValueError(f"{value} is not in list")
