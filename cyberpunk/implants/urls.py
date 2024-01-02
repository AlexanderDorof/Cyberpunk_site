from .views import *
from django.urls import path, re_path

urlpatterns = [
    path('', index, name='home'),
    path('addnewitem', addnewitem, name='addnewitem'),
    path('cat/<slug:category_path>', categories, name='categories'),
    path('cat/<slug:category_path>/<slug:category_items>', categories_items, name='categories_items'),
    path('archive/<int:item>', archive, name='archive'),

]
