from django.shortcuts import render
from django.views.generic import ListView
from .models import Item, Category, ItemImage, Color, ColorItemQuantity

class IndexView(ListView):
    model = Item
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context