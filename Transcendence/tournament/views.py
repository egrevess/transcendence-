from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from .forms import TournementForm, PlayerForm
from .models import Tournement, UserCustom, Round, Team, User
import json
from django.template.loader import render_to_string
from datetime import timedelta

# Create your views here.
def tournement(request):
	user = User.objects.get(username="emmagrev")
	user_c = UserCustom.objects.get(user=user)
	users = UserCustom.objects.all()
	try:
		tournements = Tournement.objects.all()
	except ObjectDoesNotExist:
		tournements = None
	return render(request,'tournement.html', {'tournements' : tournements, 'user':user_c, 'users': users})


def add_tour(request):
	if request.method == "POST":
		form = TournementForm(request.POST)
		if form.is_valid():
			tour = form.save(commit=False)
			start = form.cleaned_data['start']
			tour.end = start + timedelta(hours=1)
			tour.save()
			return JsonResponse({'success': True})
		else:
			return JsonResponse({'errors': form.errors.as_json()}, status=400)
	else:
		form = TournementForm()
	form_html = render_to_string(('forms/form_tournement.html'), {'form' : form}, request=request)
	return JsonResponse({'form': form_html})

def details_tournement(request, id):
	tournoi = get_object_or_404(Tournement, id=id)
	count = tournoi.players.count
	expected = tournoi.number_of_teams  * 2
	if request.method == "POST":
		form = PlayerForm(request.POST)
		if form.is_valid():
			player = form.cleaned_data['player']
			if tournoi.players.filter(id=player.id).exists():
				return JsonResponse({'success': False, 'message': "Ce joueur est déjà inscrit dans ce tournoi."}, status=400)

			if tournoi.full:
				return JsonResponse({'success': False, 'message' : "Le tournoi est complet"}, status=400)
			tournoi.players.add(player)

			if tournoi.players.count() == (tournoi.number_of_teams * 2):
				tournoi.full = True
				tournoi.save()
			data = {
				'success': True,
				'message': 'Équipe enregistrée avec succès!',
				'redirect_url': 'tournament:tournement' ,
			}
			return JsonResponse(data)
		else:
			errors = form.errors.as_json()
			print(errors)
			return JsonResponse({'success': False, 'errors': errors}, status=400)
	else:
		form = PlayerForm()
	form_html = render_to_string(('tour_details.html'), {'form' : form}, request=request)
	return render(request, 'tour_details.html', {'tournoi': tournoi, 'count' : count, 'expected': expected})

def search_players(request):
	query = request.GET.get('query', 'Default Value')
	if query:
		players = UserCustom.objects.filter(user__username__istartswith=query).order_by('user__username')[:10]  
		results = [{'id': player.user.id, 'username': player.user.username} for player in players]
		return JsonResponse(results, safe=False)
	else:
		return JsonResponse([], safe=False)
