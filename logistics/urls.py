from django.urls import path
from .views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView,
    WarehouseListView,
    WarehouseDetailView,
    WarehouseCreateView,
    WarehouseUpdateView,
    WarehouseDeleteView,
)

urlpatterns = [
    path("item/new/", ItemCreateView.as_view(), name="item_new"),
    path("item/<int:pk>/", ItemDetailView.as_view(), name="item_detail"),
    path("item/<int:pk>/edit/", ItemUpdateView.as_view(), name="item_edit"),
    path("item/<int:pk>/delete/", ItemDeleteView.as_view(), name="item_delete"),
    path("", ItemListView.as_view(), name="home"),
    path("warehouses", WarehouseListView.as_view(), name="warehouse_list"),
    path(
        "warehouses/<int:pk>/", WarehouseDetailView.as_view(), name="warehouse_detail"
    ),
    path("new/", WarehouseCreateView.as_view(), name="warehouse_new"),
    path(
        "warehouses/<int:pk>/edit/",
        WarehouseUpdateView.as_view(),
        name="warehouse_edit",
    ),
    path(
        "warehouses/<int:pk>/delete/",
        WarehouseDeleteView.as_view(),
        name="warehouse_delete",
    ),
]
