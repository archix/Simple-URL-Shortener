import unittest

from converter import Converter


class TestConverter(unittest.TestCase):

    def setUp(self):
        self.c = Converter("23456789bcdfghjkmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ-_")

    def test_shorten_and_decipher(self):
        self.assertNotEqual(self.c.shorten(10000), 10000)
        self.assertEqual(self.c.decipher(self.c.shorten(10000)), 10000)

        with self.assertRaises(TypeError):
            self.c.shorten('string, not int')
        with self.assertRaises(TypeError):
            self.c.decipher(123)


if __name__ == '__main__':
    unittest.main()
