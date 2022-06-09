import unittest
from . import factories

class MyTestCase(unittest.TestCase):

    def test_get_category(self):
        categories = factories.CategoryFactory()