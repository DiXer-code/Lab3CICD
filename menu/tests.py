from django.test import TestCase
from .models import Category, Dish

class MenuTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Десерти", description="Солодощі")
        Dish.objects.create(
            category=self.category,
            name="Чизкейк",
            price=150.00,
            is_vegetarian=True
        )

    def test_dish_creation(self):
        dish = Dish.objects.get(name="Чизкейк")
        self.assertEqual(dish.price, 150.00)
        self.assertEqual(dish.category.name, "Десерти")
        self.assertTrue(dish.is_vegetarian)