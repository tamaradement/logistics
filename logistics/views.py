from django.views.generic import ListView, DetailView
from .models import Item


class ItemListView(ListView):
    model = Item
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "item_detail.html"
