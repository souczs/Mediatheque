from django.shortcuts import render
from .models import Media

# Create your views here.
def home(request):
    tous_les_medias = Media.objects.all()
    return render(request, 'gestion/home.html', {'medias': tous_les_medias})