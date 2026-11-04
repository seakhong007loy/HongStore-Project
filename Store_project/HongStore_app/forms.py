from django import forms
from .models import Keyboard, Computer, Mouse, OrderKeyboard, OrderLaptop, OrderMouse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Add Products Forms
class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = '__all__'

class KeyboardForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = '__all__'

class MouseForm(forms.ModelForm):
    class Meta:
        model = Mouse
        fields = '__all__'

# Orders Products Forms
class OrderLaptopForm(forms.ModelForm):
    class Meta:
        model = OrderLaptop
        fields = ['location', 'phone', 'delivery']

class OrderKeyboardForm(forms.ModelForm):
    class Meta:
        model = OrderKeyboard
        fields = ['location', 'phone', 'delivery']

class OrderMouseForm(forms.ModelForm):
    class Meta:
        model = OrderMouse
        fields = ['location', 'phone', 'delivery']

# For Register 
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

