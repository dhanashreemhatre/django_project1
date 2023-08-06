from django import forms

class UserRegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'username'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"first name"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"last name"}))
    email=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'email'}))
    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'password'}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'Confirm Password'}))

class UserloginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'username'}))
    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'password'}))
    