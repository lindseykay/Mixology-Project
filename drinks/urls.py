from django.urls import path


from drinks.views import (
    DrinkListView,
    DrinkCreateView,
)

urlpatterns = [
    path("", DrinkListView.as_view(), name="drinks_list"),
    path("createdrink/", DrinkCreateView.as_view(), name="create_drink"),
]
