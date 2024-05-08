from django.db import models

# Create your models here.

#Booking Model
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    reservation_date = models.DateField()
    reservation_slot = models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.Name
    
#Category Model
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.Name

#Menu Model
class MenuItems(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    discrption = models.TextField(max_length=255, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Title
