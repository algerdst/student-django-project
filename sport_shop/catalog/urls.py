from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('project/<slug:slug>', views.product, name='product'),
]
