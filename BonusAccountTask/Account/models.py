from django.db import models
# Create your models here.


class Account(models.Model):
    first_name = models.CharField(max_length=15, verbose_name="Имя")
    second_name = models.CharField(max_length=15, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=12, verbose_name="Номер телефона")
    card_number = models.CharField(unique=True, verbose_name="Номер карты", max_length=20)
    card_balance = models.IntegerField(verbose_name="Баланс карты")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __unicode__(self):
        return self.first_name

    def __str__(self):
        return self.first_name


class Transactions(models.Model):
    types = (
        ("BonusTransaction","Оплата бонусами"),
        ("MoneyTransaction","Оплата деньгами"),
        ("EarnBonuses","Начисление бонусов")
    )
    transaction_type = models.CharField(max_length=25, verbose_name="Тип транзакции", choices=types, default="Оплата бонусами", null=False)
    transaction_sum = models.IntegerField(verbose_name="Сумма транзакции")
    transaction_date = models.DateField(verbose_name="Дата транзакции")
    transaction_user = models.ForeignKey("Account", verbose_name="Исполнитель транзакции", null=True, on_delete=models.CASCADE, related_name="transaction")

    class Meta:
        verbose_name = "Транзакции"
        verbose_name_plural = "Транзакции"

    def __str__(self):
        return self.transaction_type
