from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Account, Transactions
from .serializers import AccountSerializer
# Create your views here.


class AccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        card_number = self.request.GET.get('card_number', None)
        if card_number:
            return Account.objects.all().filter(card_number=card_number)
        else:
            return Account.objects.all().filter()

    def post(self, request, *args, **kwargs):
        return self.create(request)
