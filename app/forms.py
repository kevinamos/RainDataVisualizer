from django import forms
from .models import RainDataStore


class RainfallDataForm(forms.ModelForm):
	
	class Meta:
		model=RainDataStore
		fields=['County', 'Month', 'Rainfall_Amount']
	



class ViewCountiesForm(forms.ModelForm):
	
	class Meta:
		model=RainDataStore
		fields=['County']


class ViewmMonthsForm(forms.ModelForm):
	class Meta:

		model=RainDataStore

		fields=['Month']

