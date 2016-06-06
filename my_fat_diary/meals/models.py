from django.db import models


class FoodItem(models.Model):
    name = models.CharField(max_length=120)
    # Stores calories per 100 grams of the food
    calories = models.FloatField()
    grams = models.FloatField()


class MealItem(models.Model):
    """Stores single meal element"""
    time_eaten = models.TimeField()
    date_eaten = models.DateField()
    name = models.CharField(max_length=240)
    grams = models.FloatField(null=True, blank=True)
    calories = models.FloatField(null=True, blank=True)
    # category
    # comment
