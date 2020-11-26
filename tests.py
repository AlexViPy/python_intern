"""
app tests example

"""

from app import is_alive_host
import unittest

class TestApp(unittest.TestCase):
    def test_live(self):
        self.assertTrue (is_alive_host('semrush.com'))

    def test_down(self):
        self.assertFalse (is_alive_host('invalid.domain.son'))

if __name__ == '__main__':
    unittest.main()