from django.contrib import admin
from .models import DishCategory, Dish, DrinkCategory, Drink


admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(DrinkCategory)
admin.site.register(Drink)
