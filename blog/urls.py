from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('edit_post/<slug:slug>/', views.edit_post, name='edit_post'),
]
