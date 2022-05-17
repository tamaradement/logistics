from django.urls import path
from .views import ItemListView, ItemDetailView

urlpatterns = [
    path("item/<int:pk>/", ItemDetailView.as_view(), name="item_detail"),
    path("", ItemListView.as_view(), name="home"),
]
