"""lab_hacker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from lab_hacker.core import views as core_views
from lab_hacker.repository import views as repository_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path(r'', core_views.home, name='home'),
    path(r'get_repositories', repository_views.get_repositories, name='get_repositories'),
    path(r'edit_repository_tags/<repository_id>', repository_views.edit_repository_tags, name='edit_repository_tags'),
    path('admin/', admin.site.urls),
    path(r'login/', LoginView.as_view(), name='login'),
    path(r'logout/', LogoutView.as_view(), name='logout'),
    path(r'oauth/', include('social_django.urls', namespace='social')),
    path(r'select2/', include('django_select2.urls')),
]
