from django.db import models

# Create your models here.

class Categoria (models.model):
    idCategoria = models.IntegerField(primary_key=True,
    verbose_name='id de categoria')
    nombreCategoria = models.CharField(max_length=50,
    verbose_name='nombre de la categoria')

    def _str_(self):
        return self.nombreCategoria