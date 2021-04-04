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

    BONUS_TRANSACTION = 'BonusTransaction'
    MONEY_TRANSACTION = 'MoneyTransaction'
    EARN_BONUSES = 'EarnBonuses'

    TYPES = (
        (BONUS_TRANSACTION, "Оплата бонусами"),
        (MONEY_TRANSACTION, "Оплата деньгами"),
        (EARN_BONUSES, "Начисление бонусов")
    )

    type = models.CharField(max_length=25, verbose_name="Тип транзакции", choices=TYPES, default="Оплата бонусами", null=False)
    sum = models.IntegerField(verbose_name="Сумма транзакции")
    date = models.DateField(verbose_name="Дата транзакции")
    user = models.ForeignKey("Account", verbose_name="Исполнитель транзакции", null=True, on_delete=models.CASCADE, related_name="transactions", blank=True, default=None)

    class Meta:
        verbose_name = "Транзакции"
        verbose_name_plural = "Транзакции"

    def __str__(self):
        return self.type
