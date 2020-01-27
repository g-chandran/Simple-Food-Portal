from django.urls import path
from .views import FoodListView, SearchListView, FoodDetailView, ModelView

urlpatterns = [
    path('', FoodListView.as_view(), name='home'),
    path('search/', SearchListView.as_view(), name='search'),
    path('item/<int:pk>', FoodDetailView.as_view(), name='detail'),
    path('confirm/', ModelView.as_view(), name='confirm'),
]