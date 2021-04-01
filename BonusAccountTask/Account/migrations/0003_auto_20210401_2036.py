# Generated by Django 3.1.7 on 2021-04-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20210401_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='card_balance',
            field=models.IntegerField(editable=False, verbose_name='Баланс карты'),
        ),
        migrations.AlterField(
            model_name='account',
            name='card_number',
            field=models.CharField(editable=False, max_length=20, unique=True, verbose_name='Номер карты'),
        ),
    ]
