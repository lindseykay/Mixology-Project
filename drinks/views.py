from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Drink, Ingredient

# Create your views here.


class DrinkListView(ListView):
    model = Drink
    template_name = "drinks/list.html"
    paginate_by = 4


class DrinkCreateView(LoginRequiredMixin, CreateView):
    model = Drink
    template_name = "drinks/new.html"
    fields = [
        "name",
        "image",
        "difficulty",
        "liquor_type",
        "glass",
    ]

    def form_valid(self, form):
        new_receipe = form.save(commit=False)
        new_receipe.creator = self.request.user
        new_receipe.save()
        return redirect("create_ingredient", pk=new_receipe.id)


class DrinkCreateUpdateView(LoginRequiredMixin, UpdateView):
    model = Drink
    template_name = "drinks/ingredients.html"
    fields = ["name", "instructions"]

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except AttributeError:
            return None

    def get_success_url(self) -> str:
        return reverse_lazy("drinks_list")
