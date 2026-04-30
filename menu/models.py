from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    description = models.TextField(blank=True, verbose_name="Опис")

    def __str__(self):
        return self.name

class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=200, verbose_name="Назва страви")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")
    is_vegetarian = models.BooleanField(default=False, verbose_name="Вегетаріанська")
    is_available = models.BooleanField(default=True, verbose_name="В наявності")

    def __str__(self):
        return self.name