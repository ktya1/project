from django import forms




class UserForm(forms.Form):
    username = forms.CharField(max_length=150) #CharField - это строчка
    password = forms.CharField(widget=forms.PasswordInput)

class PhotoForm(forms.Form):
    photo = forms.ImageField(required=False)