from heap import BinaryHeap


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
