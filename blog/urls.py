"""blog_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . views import BlogsListView, BlogsDetailView, BlogsCreateView, BlogsUpdateView, BlogsDeleteView, UsersBlogsListView
from . import views

urlpatterns = [
	path( '', BlogsListView.as_view(), name = "blogs_home" ),
	path( 'user/blogs/<str:username>', UsersBlogsListView.as_view(), name = "users_blogs" ),
	path( 'about/', views.about, name = "about_blogs" ),
	path( 'blog/<pk>/', BlogsDetailView.as_view(), name = "show_blog" ),
	path( 'blog/create', BlogsCreateView.as_view(), name = "create_blog" ),
	path( 'blog/update/<pk>', BlogsUpdateView.as_view(), name = "update_blog" ),
	path( 'blog/delete/<pk>', BlogsDeleteView.as_view(), name = "delete_blog" )
]