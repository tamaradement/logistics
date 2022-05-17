from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item


class ItemListView(ListView):
    model = Item
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "item_detail.html"


class ItemCreateView(CreateView):
    model = Item
    template_name = "item_new.html"
    fields = ["type", "brand", "unit_weight", "unit_Count"]


class ItemUpdateView(UpdateView):
    model = Item
    template_name = "item_edit.html"
    fields = ["type", "brand", "unit_weight", "unit_Count"]


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "item_delete.html"
    success_url = reverse_lazy("home")
