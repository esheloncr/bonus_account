# Generated by Django 3.1.7 on 2021-04-03 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0008_auto_20210402_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='transaction_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Account.account', verbose_name='Исполнитель транзакции'),
        ),
    ]
