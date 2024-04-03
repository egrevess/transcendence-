from django.urls import path
from . import views
from .views import start_oauth

app_name = 'pong'

urlpatterns = [
    path('pong/', views.pong_view, name='pong'),
	path('start-oauth/', start_oauth, name='start-oauth'),
]