import group
import unittest

class TestCases(unittest.TestCase):

    def test_groups_of_3_1(self):
        input = [1,2,3,4,5,6,7,8,9,9]
        output = group.groups_of_3(input)
        expected = [[1,2,3],[4,5,6],[7,8,9],[9]]
        self.assertEqual(expected, output)
    def test_groups_of_3_2(self):
        input = []
        output = group.groups_of_3(input)
        expected = []
        self.assertEqual(expected, output)