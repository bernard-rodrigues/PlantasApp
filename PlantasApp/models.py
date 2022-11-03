from django.db import models

# Create your models here.
SOL_OU_SOMBRA_OPTIONS = (
    ('sp', 'Sol Pleno'),
    ('ms', 'Meia Sombra'),
    ('sb', 'Sombra')
)

class Planta(models.Model):
    nome_popular = models.CharField(max_length=255, verbose_name="Nome Popular")
    nome_cientifico = models.CharField(max_length=255, verbose_name="Nome Científico")
    sol_ou_sombra = models.CharField(max_length=2, choices=SOL_OU_SOMBRA_OPTIONS, verbose_name="Iluminação")
    intervalo_rega = models.PositiveIntegerField(verbose_name="Regas")
    ultima_rega = models.DateField(null=True, blank=True, verbose_name="Última Rega")
    proxima_rega = models.DateField(null=True, blank=True, verbose_name="Próxima Rega")
    foto_da_planta = models.ImageField(upload_to='uploads', verbose_name="Foto da Planta")
    descricao = models.TextField(verbose_name="Descrição")