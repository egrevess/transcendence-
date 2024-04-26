from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tournement, Round
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Tournement)
def create_initial_round(sender, instance, created, **kwargs):
    if created:
        try:
            Round.objects.create(name="Round 1", tournament=instance, round_number=1)
            logger.info("Round created successfully.")
        except Exception as e:
            logger.error(f"Failed to create round: {e}")

@receiver(post_save, sender=Tournement)
def tournoi_full(sender, instance, created, **kwargs):
    if instance.full and not created:  # Vérifie si le tournoi est maintenant complet et n'est pas nouvellement créé
        teams_to_create = instance.number_of_teams
        players = instance.players.all()
        
