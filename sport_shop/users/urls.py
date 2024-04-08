from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('authorization', views.authorization, name='authorization'),
    path('registration', views.registration, name='registration'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('change-password', views.change_password, name='change_password'),
]
