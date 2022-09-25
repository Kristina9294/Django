from django.db import models

class Recipe(models.Model):
    title = models.CharField('Блюдо',max_length=50,default='')
    products = models.TextField('Ингредиенты',default='')
    context = models.TextField('Рецепт',default='')

    def __str__(self):
        return self.title
