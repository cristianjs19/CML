from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from .views import HomePageView
from accounts.views import UserCreateView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='form.html', extra_context={'title':'Login'}), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('docs/', include_docs_urls(title='Books API')),
    path('schema/', get_schema_view(title="Books API"))
    # path('acuerdo/', include('books.urls')),
    # path('solicitud/', include('books.urls')),
    # path('accounts/', include('allauth.urls')),


]
