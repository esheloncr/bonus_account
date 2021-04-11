from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Account, Transactions
from .serializers import AccountSerializer, TransactionsSerializer, TransactionsToAccountSerializer


class AccountViewSet(ListModelMixin, GenericViewSet):
    queryset = Account.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = [
        "card_number",
    ]

    def get_serializer_class(self):
        if "card_number" in self.request.query_params:
            return TransactionsToAccountSerializer
        return AccountSerializer


class TransactionViewSet(ListModelMixin, GenericViewSet):
    serializer_class = TransactionsSerializer
    queryset = Transactions.objects.all()

