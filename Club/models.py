from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
Models for Pythonclubs:
Modaels become tables in the database.
Each model has an autonumbered id by default, though you can 
change that and delare you own primart keys.
I won't do that here.
Pythontype, which describes the type of Python products, laptop, tablet, software
etc. Product--the actual product,
We are going to use the Django built-in User model to store our users 
Club to store the clubs
THESE ARE NOT THE MODELS FOR PYTHON CLUB--
LOOK AT THE ASSIGNMENT
'''
class Pythontype(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.TextField(null=True, blank=True)

    def _str_(self):
        return self.typename

    class Meta:
        db_table='Pythontype'

class Product(models.Model):
    productname=models.CharField(max_length=255)
    producttype=models.ForeignKey(Pythontype, on_delete=models.DO_NOTHING)
    User=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered= models.DateField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    producturl=models.URLField()
    description=models.TextField()

   def discountAmount(self):
       self.discount=self.price* .05
       return self.discount
   
   #need to figure out why this is not working 
   #soemthing to dow with the function itsself
   def discountprice(self):
       disc=self.discountAmount()
       self.discountprice=self.price-disc
       
   def _str_(self):
        def.discountprice=self.price-self.discount
      

    class Meta:
        db_table='product'

class Club(models.Model):
    title=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    clubdata=models.DateField()
    clubtext=models.TextField()

    def _str_(self):
       return self.title

    class Meta:
        db_table='club'

