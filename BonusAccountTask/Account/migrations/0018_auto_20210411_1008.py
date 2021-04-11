# Generated by Django 3.1.7 on 2021-04-11 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0017_auto_20210404_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='user',
        ),
        migrations.AddField(
            model_name='transactions',
            name='transaction_executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction_executed', to='Account.account', verbose_name='Исполнитель транзакции'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='transaction_receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction_received', to='Account.account', verbose_name='Получатель транзакции'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='type',
            field=models.CharField(choices=[('BonusTransaction', 'Оплата бонусами'), ('MoneyTransaction', 'Оплата деньгами'), ('EarnBonuses', 'Начисление бонусов')], default='BonusTransaction', max_length=25, verbose_name='Тип транзакции'),
        ),
    ]