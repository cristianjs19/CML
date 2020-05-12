

from django.urls import path, include

from accounts.views import UserCreateView
from django.contrib.auth.views import LoginView, LogoutView




urlpatterns = [
	path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='form.html', extra_context={'title':'Login'}), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]