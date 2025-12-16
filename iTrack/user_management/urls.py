"""Direct users to appropriate urls depending on needs."""
from django.urls import path
from .views import register_view

app_name = "user_management"

urlpatterns = [
    path('register/', register_view, name='register'),
]