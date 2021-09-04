from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=15, verbose_name="Имя")
    second_name = models.CharField(max_length=15, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=12, verbose_name="Номер телефона")
    card_number = models.CharField(unique=True, verbose_name="Номер карты", max_length=20)
    card_balance = models.IntegerField(verbose_name="Баланс карты")
    is_active = models.BooleanField(default=False)

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

    STATUS_SUCCESSFUL = "SuccessTransaction"
    STATUS_UNSUCCESSFUL = "UnsuccessfulTransaction"

    STATUSES = (
        (STATUS_SUCCESSFUL, "Успешная транзакция"),
        (STATUS_UNSUCCESSFUL, "Неудачная транзакция")
    )

    type = models.CharField(max_length=25, verbose_name="Тип транзакции", choices=TYPES, default=BONUS_TRANSACTION, null=False)
    sum = models.IntegerField(verbose_name="Сумма транзакции")
    date = models.DateField(verbose_name="Дата транзакции")
    transaction_executor = models.ForeignKey("Account", verbose_name="Исполнитель транзакции", null=True,
                                             on_delete=models.CASCADE, related_name="transaction_executed", blank=True)
    transaction_receiver = models.ForeignKey("Account", verbose_name="Получатель транзакции", null=True,
                                             on_delete=models.CASCADE, related_name="transaction_received", blank=True)
    transaction_status = models.CharField(max_length=25, verbose_name="Статус транзакции", choices=STATUSES,
                                          default=STATUS_UNSUCCESSFUL, null=False)

    class Meta:
        verbose_name = "Транзакции"
        verbose_name_plural = "Транзакции"

    def __str__(self):
        return self.type
