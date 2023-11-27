from django.db import models


class DishCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='კერძების კატეგორიის სახელი')
    photo = models.ImageField(blank=True, upload_to="photos/%y/%m/%d/")

    def __str__(self):
        return self.title


class Dish(models.Model):
    title = models.CharField(max_length=50, verbose_name='კერძის სახელი')
    content = models.TextField(max_length=100, blank=True, verbose_name='აღწერა')
    weight = models.IntegerField(null=True, blank=True, verbose_name='გრამირება')
    price = models.IntegerField(blank=True, verbose_name='ფასი')
    photo = models.ImageField(blank=True, upload_to="photos/%y/%m/%d/")

    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.title


class DrinkCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='სასმელების კატეგორიის სახელი')
    photo = models.ImageField(blank=True, upload_to="photos/%y/%m/%d/")

    def __str__(self):
        return self.title


class Drink(models.Model):
    title = models.CharField(max_length=50, verbose_name='სასმელის სახელი')
    content = models.TextField(max_length=100, blank=True, verbose_name='აღწერა')
    weight = models.IntegerField(null=True, blank=True, verbose_name='გრამირება')
    price = models.IntegerField(blank=True, verbose_name='ფასი')
    photo = models.ImageField(blank=True, upload_to="photos/%y/%m/%d/")

    category = models.ForeignKey(DrinkCategory, on_delete=models.CASCADE, related_name='drinks')

    def __str__(self):
        return self.title
