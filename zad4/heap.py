class CustomHeap:
    def __init__(self, children_amount: int) -> None:
        if children_amount < 2:
            raise ValueError("At least 2 children are required per node")

        # d-ary heap
        self._d = children_amount
        self._list = []

    def __len__(self) -> int:
        return len(self._list)

    def __str__(self) -> str:
        return self._print()

    def __getitem__(self, key):
        return self._list[key]

    def push(self, value) -> None:
        """
        Appends the given element to the 'end' of the heap
        and moves the element up until heap property is restored.
        """
        self._list.append(value)
        self._shift_up(len(self) - 1)

    def _shift_up(self, index: int) -> None:
        """
        Moves an element upwards (towards the peak) until
        the heap property is restored.
        """
        item = self._list[index]
        parent_index = (index - 1) // self._d

        # move the item up until parent is smaller or equal to
        # the item, or until we reach the root
        while self._list[parent_index] > item and index > 0:
            self._list[index] = self._list[parent_index]
            index = parent_index
            parent_index = (index - 1) // self._d

        self._list[index] = item

    def _print(self, root=0, depth=0) -> str:
        result_string = ""

        leftmost_child = root * self._d + 1
        children = list(range(
            leftmost_child,
            min(len(self), leftmost_child + self._d)
        ))

        left_children = children[:self._d // 2][::-1]
        right_children = children[self._d // 2:][::-1]

        for child in right_children:
            result_string += self._print(child, depth + 4)

        result_string += " " * depth + repr(self._list[root]) + '\n'

        for child in left_children:
            result_string += self._print(child, depth + 4)

        return result_string


class BinaryHeap(CustomHeap):
    def __init__(self):
        super().__init__(2)


class TernaryHeap(CustomHeap):
    def __init__(self):
        super().__init__(3)


class QuarternaryHeap(CustomHeap):
    def __init__(self):
        super().__init__(4)
