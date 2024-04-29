from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('dilevery', views.delivery, name='delivery'),
    path('blog', views.blog, name='blog'),
    path('contacts', views.contacts, name='contacts')
]