from django.shortcuts import render
from .models import *
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

class AllFlowersView(ListView, View):
    template_name = 'index.html'
    model = Flower
    context_object_name = 'flowers'
    paginate_by = 20