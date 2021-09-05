from rest_framework import serializers
from django.contrib.auth.models import User
from Account.models import Account, Transactions


class TransactionSerializer(serializers.ModelSerializer):
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
    transactions = serializers.SerializerMethodField()

    def get_transactions(self, obj):
        current_pk = obj.pk
        executed_transactions = TransactionSerializer(Transactions.objects.filter(transaction_executor=current_pk), many=True, read_only=True).data
        received_transactions = TransactionSerializer(Transactions.objects.filter(transaction_receiver=current_pk), many=True, read_only=True).data
        data = executed_transactions + received_transactions
        return data

    class Meta:
        model = Account
        fields = [
            "first_name",
            "second_name",
            "phone_number",
            "card_number",
            "card_balance",
            "transactions",
        ]


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
