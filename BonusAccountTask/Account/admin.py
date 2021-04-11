from django.contrib import admin
from .models import Account, Transactions
from .forms import AccountCreationForm, AccountEditForm, TransactionCreationForm


@admin.register(Account)
class AdminBankAccount(admin.ModelAdmin):
    list_display = (
        "first_name",
        "second_name",
        "phone_number",
        "card_number",
        "card_balance",
    )
    search_fields = (
        "card_number",
        "second_name",
        "phone_number",
    )

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.form = AccountEditForm
        else:
            self.form = AccountCreationForm
        return super(AdminBankAccount, self).get_form(request, obj, **kwargs)


@admin.register(Transactions)
class AdminTransactions(admin.ModelAdmin):
    list_display = (
        "type",
        "sum",
        "date",
        "transaction_executor",
        "transaction_receiver",
        "transaction_status"
    )
    list_filter = (
        "type",
        "date",
        "transaction_status"
    )
    list_display_links = None
    form = TransactionCreationForm

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.transaction_receiver:
            if obj.transaction_executor == obj.transaction_receiver:
                return
            if obj.type == Transactions.BONUS_TRANSACTION:
                if obj.transaction_executor is None:
                    return
                if obj.transaction_executor.card_balance <= obj.sum:
                    return
                obj.transaction_executor.card_balance -= obj.sum
                obj.transaction_receiver.card_balance += obj.sum
                obj.transaction_status = Transactions.STATUS_SUCCESSFUL
                obj.save()
                obj.transaction_executor.save()
                obj.transaction_receiver.save()
            elif obj.type == Transactions.EARN_BONUSES:
                obj.transaction_receiver.card_balance += obj.sum
                obj.transaction_status = Transactions.STATUS_SUCCESSFUL
                obj.save()
                obj.transaction_receiver.save()
