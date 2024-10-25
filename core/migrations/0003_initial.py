# Generated by Django 5.1.2 on 2024-10-24 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total', models.CharField(max_length=255)),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('R', 'Realizado')], default='P', max_length=1)),
            ],
        ),
    ]
