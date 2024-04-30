from django.db import models

# Create your models here.

#Booking Model
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    Booking_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.Name
    
#Category Model
class Category(models.Model):
    Name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.Name

#Menu Model
class MenuItems(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Inventory = models.IntegerField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Title
