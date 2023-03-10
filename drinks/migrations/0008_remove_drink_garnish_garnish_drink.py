# Generated by Django 4.1.1 on 2022-09-22 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("drinks", "0007_alter_drink_glass_alter_drink_instructions"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="drink",
            name="garnish",
        ),
        migrations.AddField(
            model_name="garnish",
            name="drink",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="garnish",
                to="drinks.drink",
            ),
        ),
    ]
