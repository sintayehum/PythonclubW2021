from django import forms 
from .models PythonType, product, Club

class productForm(forms.modelForm):
    model=product
    field='_all_'
    
class CreateUserForm(UserCreationForm):
   class Meta:
       model = User
       fields = ['username' , 'email' , 'password1' , 'password2']  