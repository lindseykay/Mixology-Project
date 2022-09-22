from django.contrib import admin
from .models import Drink, Ingredient, Glass, Garnish

# Register your models here.


class DrinkAdmin(admin.ModelAdmin):
    pass


class IngredientAdmin(admin.ModelAdmin):
    pass


class GlassAdmin(admin.ModelAdmin):
    pass


class GarnishAdmin(admin.ModelAdmin):
    pass


admin.site.register(Drink, DrinkAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Glass, GlassAdmin)
admin.site.register(Garnish, GarnishAdmin)
