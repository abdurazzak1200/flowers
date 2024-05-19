from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

class AllFlowersView(ListView, View):
    template_name = 'index.html'
    model = Flower
    context_object_name = 'flowers'
    paginate_by = 20

    def get_queryset(self):
        queryset = self.model.objects.filter(archived=False)
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = self.model.objects.filter(title__icontains=self.request.GET.get('search', ''),
                                                 archived=False
                                                 )
            return queryset
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = self.model.objects.filter(
                archived=False,
                category=category)
            return queryset
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(AllFlowersView, self).get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context