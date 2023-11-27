from django.urls import path
from .views import DishCat, DrinkCat, DishItem, DrinkItem


urlpatterns = [
    path('', DishCat.as_view(), name='DishCat'),
    path('drinks-category/', DrinkCat.as_view(), name='DrinksCat'),
    path('dish/<int:category_id>/', DishItem.as_view(), name='DishItem'),
    path('drink/<int:category_id>/', DrinkItem.as_view(), name='DrinkItem')
]
