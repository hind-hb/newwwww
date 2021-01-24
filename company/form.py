from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from company.models import Employee


class signUpForm(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput)

    class Meta:
        model=User
        fields ={'username','email','password1','password2'}


class NewEmp(forms.ModelForm):
     name = forms.CharField(max_length=255,label='name')
     address = forms.CharField(max_length=255,label='address')
     department = forms.CharField(max_length=255,label='department')






