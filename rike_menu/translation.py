from modeltranslation.translator import register, TranslationOptions
from .models import DishCategory, Dish, DrinkCategory, Drink


@register(DishCategory)
class DishCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Dish)
class DishTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(DrinkCategory)
class DrinkCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Drink)
class DrinkTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
