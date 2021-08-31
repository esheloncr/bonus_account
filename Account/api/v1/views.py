from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from Account.models import Account, Transactions
from .serializers import AccountSerializer, TransactionsSerializer


class AccountViewSet(ListModelMixin, GenericViewSet, CreateModelMixin):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = [
        "card_number",
    ]
    permission_classes = [IsAuthenticated]


class TransactionViewSet(ListModelMixin, GenericViewSet):
    serializer_class = TransactionsSerializer
    queryset = Transactions.objects.all()

