from django.test import TestCase
from restaurantAPI.models import *


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItems.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")