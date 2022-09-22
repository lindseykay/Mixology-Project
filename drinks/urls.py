from django.urls import path


from drinks.views import (
    DrinkListView,
    DrinkCreateView,
    DrinkCreateUpdateView,
)

urlpatterns = [
    path("", DrinkListView.as_view(), name="drinks_list"),
    path("createdrink/", DrinkCreateView.as_view(), name="create_drink"),
    path("<int:pk>/edit/", DrinkCreateUpdateView.as_view(), name="create_ingredient"),
]
