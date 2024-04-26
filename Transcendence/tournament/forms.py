from django import forms
from django.forms.widgets import DateTimeInput
from django.core.exceptions import ValidationError
from .models import Tournement, Team
from pong.models import UserCustom, User

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

class PlayerForm(forms.Form):
    player = forms.CharField(required=True)
    print(f"User found: {player}")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('player')
        print(f"User found: {username}")
        try:
            user = User.objects.get(username=username)
            p = UserCustom.objects.get(user=user)
            cleaned_data['player'] = p
        except User.DoesNotExist:
            raise ValidationError("Aucun utilisateur avec ce nom d'utilisateur.")
        except UserCustom.DoesNotExist:
            raise ValidationError("Cet utilisateur n'est pas un utilisateur personnalisé valide.")
        return cleaned_data