from rest_framework import serializers
from .models import Account, Transactions


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    transaction = TransactionsSerializer(many=True)

    class Meta:
        model = Account
        fields = "__all__"
