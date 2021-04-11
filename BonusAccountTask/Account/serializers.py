from rest_framework import serializers
from .models import Account, Transactions


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):

    transaction_received = TransactionsSerializer(many=True, read_only=True)
    transaction_executed = TransactionsSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = "__all__"
