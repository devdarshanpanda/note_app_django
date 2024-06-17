from django import forms
from appone.models import Note
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class Notes_form(forms.ModelForm):
    class Meta:
        model=Note
        fields=['note_title','note_description']
        widgets={
            "note_title":forms.TextInput(attrs={"class":"form_input","placeholder":"Title"}),
            "note_description":forms.Textarea(attrs={"class":"description","placeholder":"Enter your note"})
        }
class Login_form(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-control-lg"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-control-lg"}))

class CustomerRegistrationForm(UserCreationForm):

    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={"class":"form-control form-control-lg"}))
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={"class":"form-control form-control-lg"}))
    email=forms.CharField(label='Email',widget=forms.EmailInput(attrs={"class":"form-control form-control-lg"}))
    username=forms.CharField(label='username',widget=forms.TextInput(attrs={"class":"form-control form-control-lg"}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-control-lg"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-control-lg"}))
    class Meta:
        model=User
        fields=["username","email","password1","password2","first_name","last_name"]
    