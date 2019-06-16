"""Python_Website URL Configuration

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
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as views_auth

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile , name='profile'),
    path('login/', views_auth.LoginView.as_view (template_name = 'users/login.html'), name='login'),
    path('logout/', views_auth.LogoutView.as_view (template_name = 'users/logout.html'), name='logout'),

    path('password-reset/',
        views_auth.PasswordResetView.as_view (template_name = 'users/password_reset.html'),
        name='password_reset'),

    path('password-reset/done/',
        views_auth.PasswordResetDoneView.as_view (template_name = 'users/password_reset_done.html'),
        name='password_reset_done'),

    path('password-reset/confirm<uidb64>/<token>/',
        views_auth.PasswordResetConfirmView.as_view (template_name = 'users/password_reset_confirm.html'),
        name='password_reset_confirm'),

    path('password-reset/complete/',
        views_auth.PasswordResetCompleteView.as_view (template_name = 'users/password_reset_complete.html'),
        name='password_reset_complete'),

    path('', include('blog.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
