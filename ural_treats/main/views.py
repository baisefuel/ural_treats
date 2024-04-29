from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')

def delivery(request):
    return render(request, 'delivery.html')

def blog(request):
    return render(request, 'blog.html')

def contacts(request):
    return render(request, 'contacts.html')