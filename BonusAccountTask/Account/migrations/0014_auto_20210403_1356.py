# Generated by Django 3.1.7 on 2021-04-03 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0013_auto_20210403_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='card_balance',
            field=models.IntegerField(verbose_name='Баланс карты'),
        ),
        migrations.AlterField(
            model_name='account',
            name='card_number',
            field=models.CharField(max_length=20, unique=True, verbose_name='Номер карты'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='Account.account', verbose_name='Исполнитель транзакции'),
        ),
    ]
