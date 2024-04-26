from django.db import models
from django.contrib.auth.models import User
from pong.models import UserCustom
from django.urls import reverse

class Tournement(models.Model):
	name = models.CharField(max_length=30, blank=True, null=True)
	start = models.DateTimeField()
	end = models.DateTimeField()
	players = models.ManyToManyField(UserCustom, related_name='enrolled_tournaments', blank=True)
	number_of_teams = models.IntegerField()
	full = models.BooleanField(default=False)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return f"/tournament/tournement/{self.id}/"

class Round(models.Model):
	name = models.CharField(max_length=30, blank=True, null=True)
	tournament = models.ForeignKey(Tournement, on_delete=models.CASCADE, related_name='matches')
	round_number = models.IntegerField()


class Team(models.Model):
	name = models.CharField(max_length=30, blank=True, null=True)
	round_number = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='teams')
	players = models.ManyToManyField(UserCustom, related_name='tournaments', blank=True)
	winner = models.ForeignKey(UserCustom, on_delete=models.CASCADE, null=True, blank=True, related_name='won_teams')
	

