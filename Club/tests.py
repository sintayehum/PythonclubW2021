from django.test import TestCase
from django.contrib.auth.Models import User
from .models import Pythontype, Product
import datetime
form.forms import productForm
from django.urls import reverse_lazy, reverse
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

class NewProductForm(TestCase):
    #valid form data
def test_productform(self)
    data={
           'productname':'surface', 
           'producttrype':'laptop', 
           'user':'sinta',
           'dateentered': '2021-1-5',
           'price': '1200',
           'producturl': 'http://www.microsoft.com',
           'description':'half laptop half tablet'
           
           }
   from=ProductForm (data)
   self.assertTrue(form.is_valid)
# this test is failing
def test_productform_Invalid(self):
     data={
           'productname':'surface', 
           'producttrype':'laptop', 
           'user':'sinta',
           'dateentered': 'January 2, 2020',
           'price': '1200',
           'producturl': 'http://www.microsoft.com',
           'description':'half laptop half tablet'
       }
    from=ProductForm (data)
   self.assertFalse(form.is_valid)


class New_product_Authentication_test(Clubcase):
    def setUp(self):
        self.test_user.object.Creat.user(username='testname1',password='p@ssword1')
        self.type=Type.objects.Create(typename='laptop')
        self.product.object.create((productname='Lenovo',producttype=self.type, user=self.test_user, dateentered=datetime.date(/2021,01,10),price=1200.99,producturl='http://www.lenovo.com', description="lenovo laptop"))

def test_redirect_if_not_logged_in(self):
    response=self.client.get(reverse('newproduct'))
    self.assertRedirects(response, '/accounts/login/?next=/club/newproduct/')


