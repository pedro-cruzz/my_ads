from django.forms import ModelForm
from .models import Customer, Category

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# get_user_model() garante que você pegue o CustomUser definido no settings
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Você pode adicionar campos extras aqui, caso seu CustomUser tenha
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_id', 'first_name', 'last_name', 'email', 'address', 'activebool', 'store_id', 'create_date']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_id', 'name', 'last_update']

       