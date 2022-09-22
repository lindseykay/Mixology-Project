from django.urls import path


from drinks.views import (
    DrinkListView,
)

urlpatterns = [
    path("", DrinkListView.as_view(), name="drinks_list"),
]
