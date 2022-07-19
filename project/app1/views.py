from operator import ipow
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class LoginView(TemplateView):
    template_name: str = 'app1/login.html'