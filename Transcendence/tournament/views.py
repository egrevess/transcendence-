from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from .forms import TournementForm
from .models import Tournement
import json
from django.template.loader import render_to_string
from datetime import timedelta

# Create your views here.
def tournement(request):
	try:
		tournements = Tournement.objects.all()
	except ObjectDoesNotExist:
		tournements = None
	return render(request,'tournement.html', {'tournements' : tournements})


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

def details_tournement(request, tournement_id):
	tournoi = Tournement.objects.get(id=tournement_id)
	return render(request, 'tour_details.html', {'tournoi': tournoi})
