# Generated by Django 4.2.9 on 2024-01-31 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_paciente', models.CharField(max_length=120)),
                ('idade', models.IntegerField()),
                ('peso', models.FloatField()),
                ('motivo_consulta', models.TextField()),
                ('dia_consulta', models.DateField()),
                ('hora', models.TimeField()),
                ('data_cad', models.DateTimeField(auto_now_add=True)),
                ('foto_paciente', models.ImageField(upload_to='pacientes')),
            ],
        ),
    ]