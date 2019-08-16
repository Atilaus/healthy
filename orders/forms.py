from django import forms
from .models import *

class CheckoutContactFormAnon(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True)
	
class CheckoutContactForm(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField()

class CheckoutContactForm_SAVE(forms.Form):
	name = forms.CharField(required=True)
	phone = forms.CharField(required=True)
	email = forms.CharField(required=True)