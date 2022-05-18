from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item, Warehouse


class ItemListView(ListView):
    model = Item
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "item_detail.html"


class ItemCreateView(CreateView):
    model = Item
    template_name = "item_new.html"
    fields = ["type", "brand", "unit_weight", "unit_Count", "location"]


class ItemUpdateView(UpdateView):
    model = Item
    template_name = "item_edit.html"
    fields = ["type", "brand", "unit_weight", "unit_Count", "location"]


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "item_delete.html"
    success_url = reverse_lazy("home")


class WarehouseListView(ListView):
    model = Warehouse
    template_name = "warehouse_list.html"


class WarehouseDetailView(DetailView):
    model = Warehouse
    template_name = "warehouse_detail.html"


class WarehouseCreateView(CreateView):
    model = Warehouse
    template_name = "warehouse_new.html"
    fields = ["name", "city", "state"]
    success_url = reverse_lazy("warehouse_list")


class WarehouseUpdateView(UpdateView):
    model = Warehouse
    template_name = "warehouse_edit.html"
    fields = ["name", "city", "state"]
    success_url = reverse_lazy("warehouse_list")


class WarehouseDeleteView(DeleteView):
    model = Warehouse
    template_name = "warehouse_delete.html"
    success_url = reverse_lazy("warehouse_list")
