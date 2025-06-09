from django.urls import path
from .views import home, signup_view

# accounts/urls.py
urlpatterns = [
  path('', home, name='home'),
  path('signup/', signup_view, name='signup'),
]