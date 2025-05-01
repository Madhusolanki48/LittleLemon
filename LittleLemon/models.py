from django.db import models

class Menu(models.Model):
    menu_item = models.CharField(max_length=100, default="Unnamed Dish")  # Default for menu_item
    cuisine = models.CharField(max_length=100, default="Unknown Cuisine")  # Default for cuisine
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Default for price

    def __str__(self):
        return self.menu_item
