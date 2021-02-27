from django.shortcuts import render
from .models import Item


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "base.html", context)


def checkout(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "checkout-page.html", context)


'''def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "base.html", context)'''
