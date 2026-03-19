from django.forms import ModelForm
from .models import Customer, Category

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_id', 'first_name', 'last_name', 'email', 'address', 'activebool', 'store_id', 'create_date']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_id', 'name', 'last_update']

       