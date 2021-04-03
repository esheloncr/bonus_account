from django.forms import ModelForm
from .models import Account


class AccountCreationForm(ModelForm):
    class Meta:
        model = Account
        fields = "__all__"


class AccountEditForm(ModelForm):
    class Meta:
        model = Account
        fields = (
            "first_name",
            "second_name",
            "phone_number",
        )