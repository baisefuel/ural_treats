from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
#    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
#    path('profile/', views.profile, name ='profile'),
#    path('logout/', views.logout, name='logout'),
]