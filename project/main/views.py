from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm


def index(request):
    recipe = Recipe.objects.order_by('-id')
    return render(request,'index.html',
                  {'title':'Главная страница',
                   'recipe':recipe})

def about(request):
    return render(request,'about.html')

def create(request):
    error=''
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Некорректная форма'

    form = RecipeForm()
    context = {
        'form':form,
        'error':error
    }
    return render(request,'create.html',context)

def main_detail(request, pk):
    recept = Recipe.objects.get(pk = pk)
    context = {'recept':recept}
    return render(request,'object_detail.html',
                  context=context)