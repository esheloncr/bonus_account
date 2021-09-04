from django.forms import ModelForm
from .models import Account, Transactions


class AccountCreationForm(ModelForm):
    class Meta:
        model = Account
        fields = "__all__"
        exclude = ["is_active"]


class AccountEditForm(ModelForm):
    class Meta:
        model = Account
        fields = (
            "first_name",
            "second_name",
            "phone_number",
        )


class TransactionCreationForm(ModelForm):
    class Meta:
        model = Transactions
        fields = (
            "type",
            "sum",
            "date",
            "transaction_executor",
            "transaction_receiver",
        )