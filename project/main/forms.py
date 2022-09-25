from .models import Recipe
from django.forms import ModelForm, TextInput, Textarea

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','products','context']

        widgets = {
            'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Название блюда'
        }),
            'products': Textarea(attrs={
            'class':'form-control mt-2',
            'placeholder':'Ингредиенты'
        }),
            'context': Textarea(attrs={
            'class':'form-control mt-2',
            'placeholder':'Рецепт'
        })
        }