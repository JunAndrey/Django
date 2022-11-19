from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    object_ = Phone.objects.values()

    if request.GET.get("sort") == "name":
        name = object_.order_by('name')
        return render(request, 'catalog.html', {"phones": name})

    elif request.GET.get('sort') == "max_price":
        max_price = object_.order_by('-price')
        return render(request, 'catalog.html', {"phones": max_price})

    elif request.GET.get('sort') == "min_price":
        max_price = object_.order_by('price')
        return render(request, 'catalog.html', {"phones": max_price})

    else:
        return render(request, 'catalog.html', {"phones": object_})


def show_product(request, slug):
    object_ = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {"phone": object_}
    return render(request, template, context)
