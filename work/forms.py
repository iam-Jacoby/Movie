from django import forms
from django.contrib.auth.models import User
from work.models import Genre,Movies
class Register(forms.ModelForm):
    class Meta:
        model   =   User
        fields  =   ["username","password","first_name","last_name","email"]

class Login(forms.Form):
    username    =   forms.CharField()
    password    =   forms.CharField()

class GenreForm(forms.ModelForm):
    class Meta:
        model   =   Genre
        fields  =   '__all__'

class MovieForm(forms.ModelForm):
    class Meta:
        model   =   Movies
        fields  =   '__all__'