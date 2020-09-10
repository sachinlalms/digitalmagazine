from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='magazine-home'),
    path('about/', views.about, name='magazine-about'),
]