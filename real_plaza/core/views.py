from django.shortcuts import render
from django.views import generic
from reserve.models import Sede

class HomeView(generic.TemplateView):
    template_name='index.html'
# Create your views here.
