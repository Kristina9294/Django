from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('about/', about,name='about'),
    path('create/',create,name='create'),
    path('<int:pk>/', main_detail, name='main_detail')
]