from django import forms

from PlantasApp.models import Planta

class PlantaCreateForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = [
            'nome_popular',
            'nome_cientifico',
            'sol_ou_sombra',
            'intervalo_rega',
            'foto_da_planta',
            'descricao',
        ]

        widgets = {
            'nome_popular': forms.TextInput(attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2'}),
            'nome_cientifico': forms.TextInput(attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2'}),
            'sol_ou_sombra': forms.Select(attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2'}),
            'intervalo_rega': forms.NumberInput(attrs={'class': 'border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-2', 'placeholder': 'Intervalo entre regas (dias)'}),
            'foto_da_planta': forms.FileInput(attrs={'class': 'block w-full text-sm text-lime-900 bg-lime-50 rounded-lg border border-gray-300 cursor-pointer focus:outline-none mb-2'}),
            'descricao': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500', 'rows': '4'})
        }