# Generated by Django 4.1.1 on 2022-09-22 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drinks", "0005_garnish_alter_glass_options_drink_garnish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="drink",
            name="instructions",
            field=models.TextField(blank=True),
        ),
    ]