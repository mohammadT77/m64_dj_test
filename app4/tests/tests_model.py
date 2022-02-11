from django.test import TestCase

from app4.models import Discount


# Create your tests here.
class DiscountTest(TestCase):
    def setUp(self) -> None:
        self.discount1 = Discount.objects.create(value=20, type='percent')
        self.discount2 = Discount.objects.create(value=5000, type='price')
        self.discount3 = Discount.objects.create(value=30, type='percent', max_price='10000')

    def test1_profit_price10000(self):
        self.assertEqual(self.discount1.profit_value(10000), 2000)
        self.assertEqual(self.discount2.profit_value(10000), 5000)
        self.assertEqual(self.discount3.profit_value(10000), 3000)

    def test2_profit_price100000(self):
        self.assertEqual(self.discount1.profit_value(100000), 20000)
        self.assertEqual(self.discount2.profit_value(100000), 5000)
        self.assertEqual(self.discount3.profit_value(100000), 10000)

    def test3_profit_price7000(self):
        self.assertEqual(self.discount1.profit_value(7000), 1400)
        self.assertEqual(self.discount2.profit_value(7000), 5000)
        self.assertEqual(self.discount3.profit_value(7000), 2100)

    def test4_profit_price7111(self):
        self.assertEqual(self.discount1.profit_value(7111), 1422)
        self.assertEqual(self.discount2.profit_value(7111), 5000)
        self.assertEqual(self.discount3.profit_value(7111), 2133)

    def test5_profit_price2000(self):
        self.assertEqual(self.discount1.profit_value(2000), 400)
        self.assertEqual(self.discount2.profit_value(2000), 2000)
        self.assertEqual(self.discount3.profit_value(2000), 600)


class MenuItemTest(TestCase):
    pass


class OrderTest(TestCase):
    pass
