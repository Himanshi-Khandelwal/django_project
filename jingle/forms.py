from django import forms
from jingle.models import Category
from jingle.models import UserProfile
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the category name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
		model = Category
		fields = "__all__"

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['website']
