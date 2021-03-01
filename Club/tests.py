from django.test import TestCase
from django.contrib.auth.Models import User
from .models import Pythontype, Product
import datetime
# Create your tests here.
class PythonTypeTest(TestCase):
    def setUp(self):
        self.type=Pythontype(typename='Lenovo Laptop')

    def test_Typestring(self):
        self.assertEqual(str(self.type), 'Lenovo Laptop')

    def test_tablename(self):
        self.assertEqual(str(PythonType._meta.db_table), 'pythontype')

class productTest(TestCase):
    def setUp(self):
        self.type=Pythontype(typename='Laptop')
        self.user=User(username='userl')
        self.product= product(productname='Lenovo',producttype=self.type, user=self.user, dateentered=datetime.date(/2021,01,10),price=1200.99,producturl='http://www.lenovo.com', description="lenovo laptop")

   def test_string(self):
       self.assertEqual(str(product), 'Lenovo'


   def test_discount(self);
       disc = self.product.price * .05
       self.assertEqual(self.product.discountAmount(),disc)

   def discountAmount(self):
       disc=self.product.price * (1-.05)
       self.assertEqual(self.product.discountprice(),disc)
