# Generated by Django 4.1.5 on 2023-09-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('imagen', models.ImageField(upload_to='media')),
                ('descripcion', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=30)),
                ('contraseña', models.CharField(max_length=50)),
            ],
        ),
    ]
