import unittest


def nearest_number(k, list_number):
    return min(list_number, key=lambda x: abs(x-k))


class TestNearestNumberMethods(unittest.TestCase):

    def test_nearest_number(self):
        self.assertEqual(nearest_number(10, [1, 8, 11, 15]), 11)


if __name__=="__main__":
    unittest.main()

