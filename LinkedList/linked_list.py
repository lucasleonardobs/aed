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

    def __getitem__(self, index: int) -> Node:
        i = 0
        pointer = self.head

        while pointer:
            if i == index:
                return pointer.value

            pointer = pointer.next
            i += 1

        raise IndexError("Index out of range")

    def __setitem__(self, index: int, value: int) -> None:
        i = 0
        pointer = self.head

        if index > self._size:
            raise IndexError("Index out of range")

        while pointer:
            if i == index:
                pointer.value = value

            pointer = pointer.next
            i += 1

    def push(self, value: int) -> None:
        if self.head:
            self.top.next = Node(value)
            self.top = self.top.next
        else:
            node = Node(value)
            self.head = node
            self.top = node
        self._size += 1

    def pop(self) -> Node:
        pass

    def index(self, value) -> int:
        i = 0
        pointer = self.head

        while pointer:
            if pointer.value == value:
                return i

            pointer = pointer.next
            i += 1

        raise ValueError(f"{value} is not in list")
