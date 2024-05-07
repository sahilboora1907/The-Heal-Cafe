# Generated by Django 5.0.4 on 2024-05-07 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurantAPI", "0004_category_delete_menuitems"),
    ]

    operations = [
        migrations.CreateModel(
            name="MenuItems",
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
                ("Title", models.CharField(max_length=255)),
                ("Price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("Inventory", models.IntegerField()),
                (
                    "Category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurantAPI.category",
                    ),
                ),
            ],
        ),
    ]