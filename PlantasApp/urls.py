from django.urls import path
from PlantasApp import views

urlpatterns = [
    path('minhas_plantas', views.PlantaListView.as_view(), name='planta-list'),
    path('nova_planta', views.PlantaCreateView.as_view(), name='planta-create'),
]