from django.contrib import admin
from .models import Account, Transactions
# Register your models here.


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


@admin.register(Transactions)
class AdminTransactions(admin.ModelAdmin):
    list_display = (
        "transaction_type",
        "transaction_sum",
        "transaction_date",
        "transaction_user",
    )
    list_filter = (
        "transaction_type",
        "transaction_date"
    )
    list_display_links = None
