from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls', namespace='users')),
    path('', include('main.urls', namespace='main')),
]
