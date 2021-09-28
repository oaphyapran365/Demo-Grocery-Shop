from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.utils.translation import gettext, gettext_lazy as _
from django.core import validators

def passwd_check(passwd):
    """Check if the password is valid.

    This function checks the following conditions
    if its length is greater than 6 and less than 8
    if it has at least one uppercase letter
    if it has at least one lowercase letter
    if it has at least one numeral
    if it has any of the required special symbols
    """
    SpecialSym=['$','@','#']
    return_val=True
    if len(passwd) < 8:
        raise forms.ValidationError('The length of password should be at least 8 char long')
        # return_val=False
    if not any(char.isdigit() for char in passwd):
        raise forms.ValidationError('The password should have at least one numeral')
    if not any(char.isupper() for char in passwd):
        raise forms.ValidationError('The password should have at least one uppercase letter')
       
    if not any(char.islower() for char in passwd):
        raise forms.ValidationError('The password should have at least one lowercase letter')
        
    if not any(char in SpecialSym for char in passwd):
        raise forms.ValidationError('The password should have at least one of the symbols $@#')
    if passwd[0].isdigit():
        raise forms.ValidationError('First digit cannot be number')








class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}), validators=[passwd_check])
    password2 = forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name':'Last Name', 'email':'Email'}
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget= forms.TextInput(attrs={
        'autofocus':True, 'class':'form-control'
    }))
    password = forms.CharField(label=_("Password"), strip=False,widget=forms.PasswordInput(attrs={'autocomplete':
    'current-password', 'class':'form-control'}))


