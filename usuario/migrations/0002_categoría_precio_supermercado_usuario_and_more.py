# Generated by Django 5.0.6 on 2024-07-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoría',
            fields=[
                ('ID_Categoría', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('Nombre_Catego', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('ID_Precio', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('Precio_Prod', models.PositiveIntegerField()),
                ('Fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supermercado',
            fields=[
                ('ID_Supermercado', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('Nombre_tienda', models.CharField(max_length=50, unique=True)),
                ('URL', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('ID_Usuario', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('Correo', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=50)),
                ('Nombre_User', models.CharField(max_length=50, unique=True)),
                ('Fechar_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='Descripción',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='ID_Producto',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Nombre_Produc',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
