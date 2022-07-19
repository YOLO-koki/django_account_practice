from operator import ipow
from django.urls import path
from .views import LoginView

app_name = 'app1'
urlpatterns = [
    path('', LoginView.as_view(), name='login'),
]
