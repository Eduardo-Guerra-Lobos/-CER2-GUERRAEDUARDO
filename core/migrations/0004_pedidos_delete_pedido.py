# Generated by Django 5.1.2 on 2024-10-24 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('numero_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('Total', models.CharField(max_length=255)),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('R', 'Realizado')], default='P', max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]
