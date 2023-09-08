from django.test import TestCase

from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=5, inventory=90)
        self.assertEqual(str(item), "IceCream : 5")
