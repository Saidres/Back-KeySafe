# Generated by Django 4.2.5 on 2023-10-13 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clavesFavoritas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('clave', models.CharField(max_length=30)),
                ('pista', models.CharField(max_length=255)),
            ],
        ),
    ]