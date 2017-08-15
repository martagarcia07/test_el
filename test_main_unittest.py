import unittest
from calculation import calculation
import os

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        # if field three chars are not contained in field two coded data it must fail
        line = ('pepito,"$%"%",123\n')
        result = calculation(line)
        self.assertEqual(result.calculate(line),False)

if __name__ == '__main__':
    unittest.main()