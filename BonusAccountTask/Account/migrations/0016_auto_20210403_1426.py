# Generated by Django 3.1.7 on 2021-04-03 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0015_auto_20210403_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='transaction_user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='Account.account', verbose_name='Исполнитель транзакции'),
        ),
    ]