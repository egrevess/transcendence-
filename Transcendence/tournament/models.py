from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tournement(models.Model):
	name = models.CharField(max_length=30, blank=True, null=True)
	start = models.DateTimeField()
	end = models.DateTimeField()
	teams = models.IntegerField()
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return f"/tournament/tournement/{self.id}/"

class Round(models.Model):
	name = models.CharField(max_length=30, blank=True, null=True)
	tournament = models.ForeignKey(Tournement, on_delete=models.CASCADE, related_name='matches')
	round_number = models.IntegerField()
	match_date = models.DateTimeField()


class Team(models.Model):
	round_number = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='teams')
	players = models.ManyToManyField(User, related_name='tournaments', blank=True)
	is_full = models.BooleanField(default=False)
	winner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='won_teams')
	def __str__(self):
		return f"Disponible du {self.start} au {self.end}"

	def save(self, *args, **kwargs):
		if self.players.count() >= 2:  # Nombre maximal de joueurs
			self.is_full = True
		else:
			self.is_full = False
		super().save(*args, **kwargs)
