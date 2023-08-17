from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    phone_number = forms.CharField(max_length=15, required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}))
    city = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}))
    state= forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'State'}))
    pincode=forms.CharField(max_length=10,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Pincode'}))
    address=forms.CharField(max_length=250,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    
    Gender_Choice=(('M','Male'),('F','Female'),('O','Other'))

    gender=forms.ChoiceField(choices=Gender_Choice,widget=forms.RadioSelect,required=True)

    class Meta:
        model=User
        fields=['username','email','phone_number','city','password1','password2','address','state','pincode','gender']



