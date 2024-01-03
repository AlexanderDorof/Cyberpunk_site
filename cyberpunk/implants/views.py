from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CyberwareForm


def gather_base_context():
    menus = Menu_category.objects.all()
    context = {'menus': menus,
               'shopname': 'CyberShop',
               }
    return context

def create_in_db():
    import os
    from bs4 import BeautifulSoup
    from PIL import Image
    import random


    def save_items(image_file, iter_data, number_id):
        title, description = next(iter_data)[:-1].split('|')
        title = title.strip()
        description = description.strip()
        img = 'illustration/weapons/' + image_file
        print(title, description, img)
        item = Weapon(category=title, description=description, href=number_id,
                         photo=img, weapon_category=Weapon_category.objects.get(pk=1), is_available=True,
                         damage=random.randint(2, 20),
                         load_capacity=random.randint(2, 30),
                         price=random.randint(10, 100))
        item.save()





    all_img = os.listdir(r'D:\My projects\Python\TeachMeSkills\Django_Cyberpunk\cyberpunk\media\illustration\weapons')
    with open(r'D:\My projects\Python\Learn_BeautifulSoup\cybweapons\title_description.txt') as file:
        data = file.readlines()
    iter_data = iter(data)
    number_id=200
    for image_file in all_img:
        number_id += 1
        save_items(image_file, iter_data, number_id)




def index(request):
    context = {
        'title': 'CyberShop',
    }
    context.update(gather_base_context())
    return render(request, 'implants/index.html', context=context)


def categories(request, category_path):
    dict_href = {'implants': Cyberware_category, 'trans': Auto_category, 'weapons': Weapon_category,
                 'clothes': Clothes_category, 'items': Items_category}
    chosen_category = dict_href[category_path]
    cards = chosen_category.objects.all()
    context = {
        'title': 'CyberShop',
        'cards': cards,
    }
    context.update(gather_base_context())
    return render(request, 'implants/sidemenu.html', context=context)

def categories_items(request, category_path, category_items):
    if category_items.isdigit():
        return redirect('archive', item=category_items, permanent=True)
    dict_href = {'implants': Cyberware_category, 'trans': Auto_category, 'weapons': Weapon_category,
                 'clothes': Clothes_category, 'items': Items_category}
    chosen_category = dict_href[category_path]
    x = chosen_category.objects.get(href=f"{category_path}/{category_items}")
    if category_path == 'implants':
        cards = Cyberware.objects.filter(cyberware_category=x)
    else:
        cards = Weapon.objects.filter(weapon_category=x)
    context = {
        'title': 'CyberShop',
        'cards': cards,
    }
    context.update(gather_base_context())
    return render(request, 'implants/sidemenu.html', context=context)


def archive(request, item):
    catalog = [item.href for item in Cyberware_category.objects.all()]
    dict_href = {}
    if item < 200:
        item_to_display = Cyberware.objects.filter(href=item)[0]
    else:
        item_to_display = Weapon.objects.filter(href=item)[0]
    if item in dict_href.keys():
        return redirect('home', permanent=True)
    context = {
        'title': 'Archive',
        'item': item_to_display
    }
    context.update(gather_base_context())
    return render(request, 'implants/item.html', context=context)


def addnewitem(request):
    if request.method == "POST":
        form = CyberwareForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CyberwareForm()
    context = {
        'title': 'Форма',
        'form': form
    }
    context.update(gather_base_context())
    return render(request, 'implants/forms.html', context=context)


def pageNotFoundMessage(request, exception):
    return HttpResponse("Something gone wrong...")
