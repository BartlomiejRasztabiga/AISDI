from heap import BinaryHeap, TernaryHeap, QuarternaryHeap


class TestBinaryHeap:
    def test_insert_simple(self):
        heap = BinaryHeap()
        heap.push(5)
        heap.push(1)
        heap.push(2)

        assert len(heap) == 3
        assert heap[0] == 1

    def test_insert_simple2(self):
        heap = BinaryHeap()
        heap.push(-1)
        heap.push(1)
        heap.push(-2)
        heap.push(2)
        heap.push(-3)

        assert len(heap) == 5
        assert heap[0] == -3


class TestTernaryHeap:
    def test_insert_simple(self):
        heap = TernaryHeap()
        heap.push(5)
        heap.push(1)
        heap.push(2)
        heap.push(-1)
        heap.push(10)

        assert len(heap) == 5
        assert heap[0] == -1


class TestQuaternaryHeap:
    def test_insert_simple(self):
        heap = QuarternaryHeap()
        heap.push(5)
        heap.push(1)
        heap.push(2)
        heap.push(-1)
        heap.push(10)
        heap.push(7)
        heap.push(-7)
        heap.push(9)
        heap.push(-11)

        assert len(heap) == 9
        assert heap[0] == -11
