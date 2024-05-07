# Generated by Django 5.0.4 on 2024-05-07 06:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurantAPI", "0003_alter_menuitems_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("Name", models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name="MenuItems",
        ),
    ]