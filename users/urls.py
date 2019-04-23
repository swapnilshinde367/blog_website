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

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('register/', views.register, name = "user_registration" ),
	path( 'login/', auth_views.LoginView.as_view( template_name = "users/login.html" ), name = "user_login" ),
	path( 'logout/', auth_views.LogoutView.as_view( template_name = "users/logout.html" ), name = "user_logout" ),
	path( 'password-reset/', auth_views.PasswordResetView.as_view( template_name = "users/password_reset.html" ), name = "password_reset" ),
	path( 'password-reset/done/', auth_views.PasswordResetDoneView.as_view( template_name = "users/password_reset_done.html" ), name = "password_reset_done" ),
	path( 'password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view( template_name = "users/password_reset_confirm.html" ), name = "password_reset_confirm" ),
	path( 'password-reset-complete/', auth_views.PasswordResetCompleteView.as_view( template_name = 'users/password_reset_complete.html' ), name = 'password_reset_complete' ),
	path( 'profile/',views.user_profile, name = "user_profile" ),
]