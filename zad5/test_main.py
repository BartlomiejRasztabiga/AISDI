from algorithms import find_naive, find_kmp, find_kr


class TestNaive:
    def test_simple(self):
        assert find_naive("abc", "dabcabcdddagdabdfabc") == [1, 4, 17]


class TestKMP:
    def test_simple(self):
        assert find_kmp("abc", "dabcabcdddagdabdfabc") == [1, 4, 17]


class TestKR:
    def test_simple(self):
        assert find_kr("abc", "dabcabcdddagdabdfabc") == [1, 4, 17]
