# Generated by Django 4.2.3 on 2023-10-29 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoNotaCredito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_sunat', models.CharField(max_length=2, null=True)),
                ('descripcion', models.CharField(max_length=70, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
