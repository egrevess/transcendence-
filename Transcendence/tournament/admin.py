from django.contrib import admin
from .models import Tournement
from .models import Round
from .models import Team

admin.site.register(Tournement)
admin.site.register(Round)
admin.site.register(Team)


