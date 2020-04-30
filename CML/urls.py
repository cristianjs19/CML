"""CML URL Configuration

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
from django.conf import settings
from rest_framework.documentation import include_docs_urls

from .views import HomePageView
from accounts.views import UserCreateView
from django.contrib.auth.views import LoginView, LogoutView

# from usuarios.urls import pages_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='form.html', extra_context={'title':'Login'}), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('docs/', include_docs_urls(title='My API'))
    # path('acuerdo/', include('books.urls')),
    # path('solicitud/', include('books.urls')),
    # path('accounts/', include('allauth.urls')),


]
