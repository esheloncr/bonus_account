from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(models.Model):
    first_name = models.CharField(max_length=15, verbose_name="Имя")
    second_name = models.CharField(max_length=15, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=12, verbose_name="Номер телефона")
    card_number = models.CharField(unique=True, verbose_name="Номер карты", max_length=20,editable=False)
    card_balance = models.IntegerField(verbose_name="Баланс карты",editable=False)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Transactions(models.Model):
    types = (
        ("BonusTransaction","Оплата бонусами"),
        ("MoneyTransaction","Оплата деньгами"),
        ("EarnBonuses","Начисление бонусов")
    )
    transaction_type = models.CharField(max_length=25,verbose_name="Тип транзакции",choices=types,default="Оплата бонусами",null=False)
    transaction_sum = models.IntegerField(verbose_name="Сумма транзакции")
    transaction_date = models.DateField(verbose_name="Дата транзакции")
    transaction_user = models.ForeignKey(User,verbose_name="Исполнитель транзакции",on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = "Транзакции"
