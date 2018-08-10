"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from posts.views import posts_list, post_detail, post_add, search_posts, edit_post
from accounts.views import register
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', posts_list, name='home'),
    path('', posts_list, name='posts_list'),
    path('post/<int:id>', post_detail, name="post_detail"),
    path('post/<int:id>/edit', edit_post, name="edit_post"),
    path('post/add', post_add, name="post_add"),
    path('search', search_posts, name="search_posts"),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
   

]
