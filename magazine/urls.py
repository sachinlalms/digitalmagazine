from django.urls import path
from . import views
from .views import PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.Postlist.as_view(), name='magazine-home'),
    path('about/', views.about, name='magazine-about'),
    path('post/<int:pk>/',views.PostDetail.as_view(),name='post-details'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]