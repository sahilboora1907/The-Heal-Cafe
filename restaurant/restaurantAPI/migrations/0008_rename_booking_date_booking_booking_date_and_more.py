# Generated by Django 5.0.6 on 2024-05-08 05:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("restaurantAPI", "0007_alter_booking_booking_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="Booking_date",
            new_name="booking_date",
        ),
        migrations.RenameField(
            model_name="booking",
            old_name="Name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="booking",
            old_name="No_of_guests",
            new_name="no_of_guests",
        ),
        migrations.RenameField(
            model_name="category",
            old_name="Name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="menuitems",
            old_name="Category",
            new_name="category",
        ),
        migrations.RenameField(
            model_name="menuitems",
            old_name="Discrption",
            new_name="discrption",
        ),
        migrations.RenameField(
            model_name="menuitems",
            old_name="Inventory",
            new_name="inventory",
        ),
        migrations.RenameField(
            model_name="menuitems",
            old_name="Price",
            new_name="price",
        ),
        migrations.RenameField(
            model_name="menuitems",
            old_name="Title",
            new_name="title",
        ),
    ]