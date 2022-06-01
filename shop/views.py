from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item, Category, ItemImage, Color, ColorItemQuantity, Brand

class IndexView(ListView):
    model = Item
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ItemImage.objects.filter(item=self.get_object())
        context['colors'] = ColorItemQuantity.objects.filter(item=self.get_object())
        context['related_items'] = Item.objects.filter(category=self.get_object().category)
        return context


class ItemListView(ListView):
    model = Item
    template_name = 'store.html'

    def get_queryset(self):
        queryset = self.model.objects.all()
        price_min = self.request.GET.get('price-min')
        price_max = self.request.GET.get('price-max')
        if price_min and price_max:
            queryset = queryset.filter(price__gt=price_min, price__lte=price_max)
            category_ids = []
            brands_ids = []
            for name in self.request.GET.keys():
                if name.startswith('category'):
                    category_ids.append(int(name.split('-')[1]))
                elif name.startswith('brand'):
                    brands_ids.append(int(name.split('-')[1]))
            if category_ids:
                queryset = queryset.filter(category__in=category_ids)
            if brands_ids:
                queryset = queryset.filter(brand__in=brands_ids)
        return queryset



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        return context


def test(request):
    print(request.GET)
    return HttpResponse("OK")