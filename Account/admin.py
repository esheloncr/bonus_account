from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.utils.html import format_html
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
        "account_actions",
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

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("accept/<int:pk>", self.accept_user),
            path("decline/<int:pk>", self.decline_user),
        ]
        return custom_urls + urls

    def account_actions(self, obj):
        if obj.is_active:
            return format_html(
                f"<a href='{obj.pk}/delete' class='button'>Remove account</a>"
            )
        return format_html(
            f"<a href='accept/{obj.pk}' class='button'>Accept</a>"
            f"<a href='decline/{obj.pk}' class='button'>Decline</a>"
        )

    account_actions.short_description = "Действия с аккаунтом"

    def accept_user(self, request, pk):
        self.model.objects.filter(pk=pk).update(is_active=True)
        return redirect("../")

    def decline_user(self, request, pk):
        self.model.objects.filter(pk=pk).update(is_active=False)
        return redirect(f"../{pk}/delete")


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
