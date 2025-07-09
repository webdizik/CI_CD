from django.urls import path

from . import views as blog_views
from authentication import views as auth_views

urlpatterns = [
    path('', blog_views.post_list, name='post_list'),
    path('post/new/', blog_views.post_new, name='post_new'),
    path('post/<int:pk>/', blog_views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', blog_views.post_edit, name='post_edit'),
]