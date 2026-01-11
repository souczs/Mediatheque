from django.contrib import admin
from .models import Membre, Media, Livre, Dvd, Cd, JeuDePlateau

# Register your models here.
admin.site.register(Membre)
admin.site.register(Livre)
admin.site.register(Dvd)
admin.site.register(Cd)
admin.site.register(JeuDePlateau)