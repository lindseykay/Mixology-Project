# Generated by Django 4.1.1 on 2022-09-20 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("drinks", "0004_glass_alter_ingredient_amount_drink_glass"),
    ]

    operations = [
        migrations.CreateModel(
            name="Garnish",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name_plural": "garnish",
            },
        ),
        migrations.AlterModelOptions(
            name="glass",
            options={"verbose_name_plural": "glasses"},
        ),
        migrations.AddField(
            model_name="drink",
            name="garnish",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="drink",
                to="drinks.garnish",
            ),
        ),
    ]
