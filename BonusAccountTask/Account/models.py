from django.db import models

# Create your models here.


class Account(models.Model):
    first_name = models.CharField(max_length=15, verbose_name="Имя")
    second_name = models.CharField(max_length=15, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=12, verbose_name="Номер телефона")
    card_number = models.CharField(unique=True, verbose_name="Номер карты", max_length=20,editable=False)
    card_balance = models.IntegerField(verbose_name="Баланс карты",editable=False)


class Transactions(models.Model):
    transaction_type = None
    transaction_sum = models.IntegerField(verbose_name="Сумма транзакции",editable=False)
    transaction_date = models.DateField(verbose_name="Дата транзакции")
    transaction_user = None
