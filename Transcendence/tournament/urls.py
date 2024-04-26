from django.urls import path
from . import views
from .views import add_tour

app_name = 'tournament'

urlpatterns = [
    path('tournement/', views.tournement, name='tournement'),
	path('add_tour/', views.add_tour, name='add_tour'),
	path('tournement/<int:id>/', views.details_tournement, name='details_tournement'),
	path('search_players/', views.search_players, name='search_players'),
]