from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Account
from .serializers import AccountSerializer
# Create your views here.


class AccountView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        card_number = self.request.GET.get('card_number', None)
        if card_number:
            return Account.objects.all().filter(card_number__contains=card_number)
        else:
            return Account.objects.all()
