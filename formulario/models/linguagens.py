from django.db import models

class Linguagens(models.Model):
    class Linguagem:
        cpp = 'C++'
        csharp = 'C#'
        js = 'Javascript'
        php = 'PHP'
        py = 'Python'
        ruby = 'Ruby'
        java = 'Java'
        outros = 'Outros'

    linguagens = models.CharField(max_length=10, choices=[
        (Linguagem.cpp, 'C++'),
        (Linguagem.csharp, 'C#'),
        (Linguagem.js, 'Javascript'),
        (Linguagem.php, 'PHP'),
        (Linguagem.py, 'Python'),
        (Linguagem.ruby, 'Ruby'),
        (Linguagem.java, 'Java'),
        (Linguagem.outros, 'Outros'),
    ])

    def __str__(self) -> str:
        return self.linguagens