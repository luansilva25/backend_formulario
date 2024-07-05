from django.contrib import admin
from .models import Estados, Formulario, Hobbies, Linguagens

@admin.register(Estados)
class Estados(admin.ModelAdmin):
    list_display = ('id', 'estado', )

@admin.register(Formulario)
class Estados(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'nascimento', 'cidade', 'estado', 'endereco', )
 
@admin.register(Linguagens)
class Estados(admin.ModelAdmin):
    list_display = ('id', 'linguagens', )

@admin.register(Hobbies)
class Estados(admin.ModelAdmin):
    list_display = ('id', 'hobby', )