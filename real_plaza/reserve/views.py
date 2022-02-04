from django.shortcuts import render
from django.views import generic

class ReserveView(generic.TemplateView):
    template_name='reservas.html'
# Create your views here.
