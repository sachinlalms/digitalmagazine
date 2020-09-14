from django.urls import path
from . import views


urlpatterns = [
    path('', views.Postlist.as_view(), name='magazine-home'),
    path('about/', views.about, name='magazine-about'),
    path('post/<int:pk>/',views.PostDetail.as_view(),name='post-details'),

]