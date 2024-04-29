from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator
from products.utils import search

from .models import Products

def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    
    if category_slug == "all":
        products = Products.objects.all()
    elif query:
        products = search(query)
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if order_by and order_by != "default":
        products = products.order_by(order_by)

    paginator = Paginator(products, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug
    }
    return render(request, "products/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {"product": product}

    return render(request, "productPage.html", context=context)