# Generated by Django 5.0.8 on 2024-09-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vivero', '0004_labor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoControlHongo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_ica', models.CharField(max_length=50)),
                ('nombre_producto', models.CharField(max_length=100)),
                ('frecuencia_aplicacion', models.CharField(max_length=50)),
                ('valor_producto', models.FloatField()),
                ('periodo_carencia', models.IntegerField()),
                ('nombre_hongo', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
