from django import forms
from .models import *

class CheckoutContactFormAnon(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True)
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		username_qs = User.objects.filter(username=email)
		if username_qs.exists():
			raise forms.ValidationError('This email is already being used')
		return email

class CheckoutContactForm(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField()

class CheckoutContactForm_SAVE(forms.Form):
	name = forms.CharField(required=True)
	phone = forms.CharField(required=True)
	email = forms.CharField(required=True)