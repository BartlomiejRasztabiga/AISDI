from algorithms import find_naive, find_kmp, find_kr
import random


class TestNaive:
    def test_simple(self):
        assert find_naive("abc", "dabcabcdddagdabdfabc") == [1, 4, 17]

    def test_empty_substring(self):
        assert find_naive("", "dabcabcdddagdabdfabc") == []

    def test_empty_text(self):
        assert find_naive("abcd", "") == []

    def test_empty_both(self):
        assert find_naive("", "") == []

    def test_both_equal(self):
        assert find_naive("abcd", "abcd") == [0]

    def test_substring_longer(self):
        assert find_naive("abcdefg", "abc") == []

    def test_no_substring_in_text(self):
        assert find_naive("abc", "abdcefg") == []

    def test_match_single1(self):
        assert find_naive("ab", "abcdefgh") == [0]

    def test_match_single2(self):
        assert find_naive("ab", "edcdbabefgh") == [5]

    def test_match_single3(self):
        assert find_naive("ab", "ba34a12aasadyabds") == [13]

    def test_match_overlap(self):
         assert find_naive("aba", "abababcefgababa") == [0, 2, 10, 12]


class TestKMP:
    def test_simple(self):
        assert find_kmp("abc", "dabcabcdddagdabdfabc") == [1, 4, 17]

    def test_empty_substring(self):
        assert find_kmp("", "dabcabcdddagdabdfabc") == []

    def test_empty_text(self):
        assert find_kmp("abcd", "") == []

    def test_empty_both(self):
        assert find_kmp("", "") == []

    def test_both_equal(self):
        assert find_kmp("abcd", "abcd") == [0]

    def test_substring_longer(self):
        assert find_kmp("abcdefg", "abc") == []

    def test_no_substring_in_text(self):
        assert find_kmp("abc", "abdcefg") == []


class TestKR:
    def test_simple(self):
        assert find_kr("abc", "dabcabcdddagdabdfabc") == [1, 4, 17]

    def test_empty_substring(self):
        assert find_kr("", "dabcabcdddagdabdfabc") == []

    def test_empty_text(self):
        assert find_kr("abcd", "") == []

    def test_empty_both(self):
        assert find_kr("", "") == []

    def test_both_equal(self):
        assert find_kr("abcd", "abcd") == [0]

    def test_substring_longer(self):
        assert find_kr("abcdefg", "abc") == []

    def test_no_substring_in_text(self):
        assert find_kr("abc", "abdcefg") == []


class TestRandomData:
    def generate_random_string(self, length: int):
        alphabet = ['A', 'Z']
        return [random.choice(alphabet) for x in range(length)]

    def test_all_algorithms(self):
        substring = self.generate_random_string(10)
        text = self.generate_random_string(100)

        naive_res = find_naive(substring, text)
        kr_res = find_kr(substring, text)
        kmp_res = find_kmp(substring, text)

        assert naive_res == kr_res == kmp_res
