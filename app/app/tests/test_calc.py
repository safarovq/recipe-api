from django.test import SimpleTestCase
from app import calc


class TestCalc(SimpleTestCase):
    def test_add(self):
        res = calc.add(3, 5)

        self.assertEqual(res, 8)
