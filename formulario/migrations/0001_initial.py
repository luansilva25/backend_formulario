# Generated by Django 5.0.6 on 2024-07-04 01:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Acre', 'AC'), ('Alagoas', 'AL'), ('Amapá', 'AP'), ('Amazonas', 'AM'), ('Bahia', 'BA'), ('Ceará', 'CE'), ('Distrito Federal', 'DF'), ('Espírito Santo', 'ES'), ('Goiás', 'GO'), ('Maranhão', 'MA'), ('Mato Grosso', 'MT'), ('Mato Grosso do Sul', 'MS'), ('Minas Gerais', 'MG'), ('Pará', 'PA'), ('Paraíba', 'PB'), ('Paraná', 'PR'), ('Pernambuco', 'PE'), ('Piauí', 'PI'), ('Rio de Janeiro', 'RJ'), ('Rio Grande do Norte', 'RN'), ('Rio Grande do Sul', 'RS'), ('Rondônia', 'RO'), ('Roraima', 'RR'), ('Santa Catarina', 'SC'), ('São Paulo', 'SP'), ('Sergipe', 'SE'), ('Tocantins', 'TO')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(choices=[('ler', 'Ler'), ('cantar', 'Cantar'), ('dançar', 'Dançar'), ('jogar', 'jogar'), ('praticar esportes', 'Praticar'), ('tocar estrumentos musicais', 'Tocar estrumentos musicais'), ('programar', 'Programar'), ('outros', 'Outras')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Linguagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linguagens', models.CharField(choices=[('C++', 'C++'), ('C#', 'C#'), ('Javascript', 'Javascript'), ('PHP', 'PHP'), ('Python', 'Python'), ('Ruby', 'Ruby'), ('Java', 'Java'), ('Outros', 'Outros')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('senha', models.CharField(max_length=25)),
                ('endereco', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=50)),
                ('nascimento', models.DateField()),
                ('biografia', models.TextField(blank=True, max_length=1000, null=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulario.estados')),
                ('hobbies', models.ManyToManyField(to='formulario.hobbies')),
                ('linguagem', models.ManyToManyField(to='formulario.linguagens')),
            ],
        ),
    ]