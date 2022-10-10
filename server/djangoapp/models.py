from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null= False, max_length=20, default='')
    description = models.CharField(null= False, max_length=250, default='')
    def __str__(self):
        return 'Name:' + self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    make = models.ForeignKey(CarMake, null= True, on_delete=models.CASCADE)
    name = models.CharField(null= False, max_length=35, default='')
    dealerid = models.IntegerField(null=True)
    sedan = 'sedan'
    suv = 'suv'
    wagon = 'wagon'
    other = 'other'
    types = [(sedan, "Sedan"), (suv, 'SUV'), (wagon, 'Wagon'), (other, 'Other')]
    cartype = models.CharField(null= False, max_length=20, choices= types, default=other)
    year = models.DateField(null= True)
    def __str__(self):
        return 'Name ' + self.name

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
