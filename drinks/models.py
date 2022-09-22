from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL

# Create your models here.


class Drink(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    image = models.URLField(blank=False)
    instructions = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(
        USER_MODEL, related_name="drinks", on_delete=models.CASCADE, null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    glass = models.ForeignKey(
        "Glass", related_name="drink", on_delete=models.PROTECT, null=True, blank=True
    )

    EASY = "1"
    MODERATE = "2"
    ADVANCED = "3"

    difficulty_choices = [
        (EASY, "easy"),
        (MODERATE, "moderate"),
        (ADVANCED, "advanced"),
    ]

    difficulty = models.CharField(max_length=2, choices=difficulty_choices, blank=False)

    WHISKEY = "W"
    VODKA = "V"
    TEQUILA = "T"
    RUM = "R"
    GIN = "G"
    BRANDY = "B"
    OTHER = "O"

    liquor_choices = [
        (WHISKEY, "Whiskey"),
        (VODKA, "Vodka"),
        (TEQUILA, "Tequila"),
        (RUM, "Rum"),
        (GIN, "Gin"),
        (BRANDY, "Brandy"),
        (OTHER, "Other"),
    ]

    liquor_type = models.CharField(max_length=2, choices=liquor_choices, blank=False)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    amount = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=300)
    drink = models.ForeignKey(Drink, related_name="drinks", on_delete=models.CASCADE)

    def __str__(self):
        if self.amount:
            return f"{self.amount} of {self.name}"
        else:
            return self.name


class Glass(models.Model):
    class Meta:
        verbose_name_plural = "glasses"

    type = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.type


class Garnish(models.Model):
    class Meta:
        verbose_name_plural = "garnish"

    name = models.CharField(max_length=200)
    drink = models.ForeignKey(
        "Drink", related_name="garnish", on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return self.name
