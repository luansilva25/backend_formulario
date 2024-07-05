from django.db import models
from .hobbies import Hobbies
from .linguagens import Linguagens
from .estado import Estados

class Formulario(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    senha = models.CharField(max_length=25)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    hobbies = models.ManyToManyField(Hobbies)
    nascimento = models.DateField()
    linguagem = models.ManyToManyField(Linguagens)
    estado  = models.ForeignKey(Estados, on_delete=models.CASCADE)
    biografia = models.TextField(max_length=1000, null=True, blank=True)

