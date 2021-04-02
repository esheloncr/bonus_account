from rest_framework import serializers
from .models import Account, Transactions


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"