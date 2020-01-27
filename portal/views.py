from .models import Food
from django.views.generic import ListView, DetailView, TemplateView

class FoodListView(ListView):
    model = Food
    template_name = 'home.html'

class SearchListView(ListView):
    model = Food
    template_name = 'search.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        return Food.objects.filter(food_name__icontains=query)

class FoodDetailView(DetailView):
    model = Food
    template_name = 'detail.html'

class ModelView(TemplateView):
    template_name = "confirm.html"
