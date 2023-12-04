import unittest
from name_function import get_formatted_name

class NameTestClass(unittest.TestCase):
    """name_function.pyをテストする"""

    def test_first_last_name(self):
        """Janis Jpolin のような名前で動作するか？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Wolfgang Amadeus Mozart のような名前で動作するか？"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
