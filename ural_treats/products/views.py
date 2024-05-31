from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.core.paginator import Paginator
from products.utils import search
from .models import Products, Categories

def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    categories = Categories.objects.all()

    if query:
        products = Products.objects.filter(name__icontains=query)
    elif category_slug:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    else:
        products = Products.objects.all()


    if order_by and order_by != "default":
        products = products.order_by(order_by)

    paginator = Paginator(products, 12)
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Каталог",
        "products": current_page,
        "categories": categories,
        "selected_category": category_slug,
        "query": query
    }
    return render(request, "catalog.html", context)

def product(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)

    context = {"product": product}

    return render(request, "productPage.html", context=context)
