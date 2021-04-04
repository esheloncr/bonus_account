from django.contrib import admin
from .models import Account, Transactions
from .forms import AccountCreationForm,AccountEditForm
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
        "user",
    )
    list_filter = (
        "type",
        "date"
    )
    list_display_links = None
