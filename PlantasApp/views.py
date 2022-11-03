from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from PlantasApp.forms import PlantaCreateForm

from PlantasApp.models import Planta

# Create your views here.
class PlantaListView(ListView):
    model = Planta
    template_name = 'PlantasApp/planta_list.html'

class PlantaCreateView(CreateView):
    model = Planta
    form_class = PlantaCreateForm
    template_name = 'PlantasApp/planta_create.html'