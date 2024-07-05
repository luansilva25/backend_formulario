from django.db import models

class Hobbies(models.Model):
    class Hobby:
        Ler = 'ler'
        Cantar = 'cantar'
        Dancar = 'dançar'
        Jogar = 'jogar'
        Praticar = 'praticar esportes'
        Instrumento = 'tocar estrumentos musicais'
        Programar = 'programar'
        Outras = 'outros'

    hobby = models.CharField(max_length=50, choices=[
            (Hobby.Ler, 'Ler'),
            (Hobby.Cantar, 'Cantar'),
            (Hobby.Dancar, 'Dançar'),
            (Hobby.Jogar, 'jogar'),
            (Hobby.Praticar, 'Praticar'),
            (Hobby.Instrumento, 'Tocar estrumentos musicais'),
            (Hobby.Programar, 'Programar'),
            (Hobby.Outras, 'Outras'),
        ])
    
    def __str__(self) -> str:
        return self.hobby