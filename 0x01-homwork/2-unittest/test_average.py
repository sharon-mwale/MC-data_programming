import unittest
from average import average 

class TestAver(unittest.TestCase):

    def test_total(self):
        sample_list = [4, 8, 9, 15]
        result = average(sample_list)
        self.assertEqual(result, 9)

if __name__ == "__main__":
    unittest.main()
