from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Drink

# Create your views here.


class DrinkListView(ListView):
    model = Drink
    template_name = "drinks/list.html"
    paginate_by = 4
