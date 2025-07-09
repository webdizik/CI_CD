from django.urls import path

from . import views as auth_views
from blog import views as blog_views


urlpatterns = [
    path('', auth_views.home, name='home'),
    path('login/', auth_views.login_page, name='login_page'),
    path('register/', auth_views.register_page, name='register_page'),
    path('blog/', blog_views.post_list, name='post_list'),
]