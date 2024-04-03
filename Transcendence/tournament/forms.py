from django import forms
from django.forms.widgets import DateTimeInput
from .models import Tournement

class TournementForm(forms.ModelForm):
	class Meta:
		model = Tournement
		exclude = ['end']
		widgets = {
			'start': DateTimeInput(attrs={'type': 'datetime-local'}),
		}

	def clean(self):
		cleaned_data = super().clean()
		teams = cleaned_data.get('teams')
		if teams not in [1,2, 4]:
			raise forms.ValidationError("Le nombre d'équipes doit être soit 1, 2 ou 4.")