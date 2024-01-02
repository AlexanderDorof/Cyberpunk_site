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

def add_item_test():
    item = Cyberware(category='katamaran', description='tatatatat', href='implants',photo='illustration/Menu_preview/Moto.jpg', Characteristic="BODY", is_available=True, capacity=10, price=10, cyberware_category=Cyberware_category.objects.get(pk=1))
    item.save()




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
    # if '/' in category_path:
    #     category_path = category_path.split('/')[1]
    #     if category_path.isdigit():
    #         return redirect('archive', item=category_path, permanent=True)
    #     chosen_category = dict_href[category_path]
    # else:
    #     chosen_category = dict_href[category_path]
    cards = chosen_category.objects.all()
    context = {
        'title': 'CyberShop',
        'cards': cards,
    }
    context.update(gather_base_context())
    return render(request, 'implants/sidemenu.html', context=context)

def categories_items(request, category_path, category_items):
    dict_href = {'implants': Cyberware_category, 'trans': Auto_category, 'weapons': Weapon_category,
                 'clothes': Clothes_category, 'items': Items_category}
    chosen_category = dict_href[category_path]
    x = Cyberware_category.objects.get(href=f"{category_path}/{category_items}")
    cards = Cyberware.objects.filter(cyberware_category=x)
    context = {
        'title': 'CyberShop',
        'cards': cards,
    }
    context.update(gather_base_context())
    return render(request, 'implants/sidemenu.html', context=context)


def archive(request, item):
    catalog = [item.href for item in Cyberware_category.objects.all()]
    dict_href = {}
    item_to_display = Cyberware.objects.filter(href=item)[0]
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
