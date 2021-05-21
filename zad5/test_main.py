from algorithms import find_naive


class TestNaive:
    def test_simple(self):
        assert find_naive("abc", "dabcabcdddagdabdfabc") == [1, 4, 17]


class TestKMP:
    def test_simple(self):
        pass


class TestKR:
    def test_simple(self):
        pass
