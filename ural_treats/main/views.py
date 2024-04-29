from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')

def delivery(request):
    return render(request, 'delivery.html')