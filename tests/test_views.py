from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        # create a test user for authentication
        user = User.objects.create(username="testuser", password="12345")
        # init the test api client
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        # create menu model objects
        Menu.objects.create(title="IceCream", price=5, inventory=90)
        Menu.objects.create(title="Cake", price=10, inventory=100)
        Menu.objects.create(title="Omlette", price=2, inventory=50)

    def test_getall(self):
        url = reverse("menu-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        serializer = MenuSerializer(data=response.data, many=True)
        self.assertEqual(serializer.is_valid(), True)

        menu = Menu.objects.all()
        self.assertEqual(len(menu), len(serializer.validated_data))

        for expected_menu_item, actual_menu_item in zip(
            menu, serializer.validated_data
        ):
            self.assertEqual(actual_menu_item["title"], expected_menu_item.title)
            self.assertEqual(actual_menu_item["price"], expected_menu_item.price)
            self.assertEqual(
                actual_menu_item["inventory"], expected_menu_item.inventory
            )
