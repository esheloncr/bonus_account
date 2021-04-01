from django.contrib import admin
from .models import Account
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