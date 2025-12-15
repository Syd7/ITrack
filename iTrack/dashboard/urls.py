"""Direct users to appropriate urls depending on needs."""
from django.urls import path
from .views import dashboard_View

app_name = "dashboard"

urlpatterns = [
    path('dashboard/', dashboard_View, name='dashboard'),
]