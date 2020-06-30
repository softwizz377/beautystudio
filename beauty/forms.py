from django import forms
from beauty.models import contact, appointment,feedback,service,FAQs,career
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class contactform(forms.ModelForm):
	firstname=forms.CharField(max_length=200)
	lastname=forms.CharField(max_length=200)
	phone=forms.CharField(max_length=200)
	city=forms.CharField(max_length=200)

	
	class Meta:
		model=contact
		fields="__all__"

class appointmentform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	email=forms.CharField(max_length=200)
	date=forms.CharField(max_length=200)
	time=forms.CharField(max_length=200)
	appointmentfor=forms.CharField(max_length=200)
	appointmentplace=forms.CharField(max_length=200)
	class Meta:
		model=appointment
		fields="__all__"
		
class feedbackform(forms.ModelForm):
	experience=forms.CharField(max_length=200)
	name=forms.CharField(max_length=200)
	email=forms.CharField(max_length=200)
	phone=forms.CharField(max_length=200)
	message=forms.CharField(max_length=200)
	
	
	class Meta:
		model=feedback
		fields="__all__"
		
class FAQsform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	mobile=forms.CharField(max_length=200)
	class Meta:
		model=FAQs
		fields="__all__"
		
class careerform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	email=forms.CharField(max_length=200)
	gender=forms.CharField(max_length=200)
	address=forms.CharField(max_length=200)
	phone=forms.CharField(max_length=200)
	sentfile=forms.FileField()
	class Meta:
		model=career
		fields="__all__"
		