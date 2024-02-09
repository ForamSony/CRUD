from django import forms
from .models import student
from django.contrib.auth.forms import 

class studentregistration(forms.ModelForm):
    
    class Meta:
        model = student
        fields = ['name','email','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),

        }
