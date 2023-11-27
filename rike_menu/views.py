from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView


class DishCat(ListView):
    model = DishCategory
    template_name = 'rike_menu/dish-category.html'
    context_object_name = 'dishcat'

    def get_queryset(self):
        return DishCategory.objects.all()


class DrinkCat(ListView):
    model = DrinkCategory
    template_name = 'rike_menu/drinks-category.html'
    context_object_name = 'drinkcat'

    def get_queryset(self):
        return DrinkCategory.objects.all()


class DishItem(ListView):
    model = Dish
    template_name = 'rike_menu/dish.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        category = get_object_or_404(DishCategory, id=self.kwargs['category_id'])
        return Dish.objects.filter(category=category)


class DrinkItem(ListView):
    model = Drink
    template_name = 'rike_menu/drink.html'
    context_object_name = 'drink'

    def get_queryset(self):
        return Drink.objects.all()


