from rest_framework import serializers
from django.contrib.auth.models import User
from Account.models import Account, Transactions


class TransactionsSerializer(serializers.ModelSerializer):
    executor_first_name = serializers.SerializerMethodField(read_only=True)
    receiver_first_name = serializers.SerializerMethodField(read_only=True)

    def get_executor_first_name(self, obj):
        try:
            return obj.transaction_executor.first_name
        except AttributeError:
            return "Not specified"

    def get_receiver_first_name(self, obj):
        try:
            return obj.transaction_receiver.first_name
        except AttributeError:
            return "Not specified"

    class Meta:
        model = Transactions
        fields = [
            "type",
            "sum",
            "date",
            "executor_first_name",
            "receiver_first_name",
            "transaction_status",
        ]


class AccountSerializer(serializers.ModelSerializer):
    transaction_received = TransactionsSerializer(many=True, read_only=True)
    transaction_executed = TransactionsSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = [
            "first_name",
            "second_name",
            "phone_number",
            "card_number",
            "card_balance",
            "transaction_received",
            "transaction_executed"
        ]


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]
