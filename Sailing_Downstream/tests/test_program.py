import unittest
from main import process_list

class TestProcessList(unittest.TestCase):

    def test_valid_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Valid input (length is multiple of 10)
        result = process_list(input_list)
        self.assertEqual(result, [1, 3, 5, 7, 9])

    def test_invalid_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Invalid input (length is not multiple of 10)
        with self.assertRaises(ValueError):
            process_list(input_list)

    # Add more test methods for corner cases and edge cases

if __name__ == '__main__':
    unittest.main()
