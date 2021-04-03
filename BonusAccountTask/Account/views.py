from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account
from .serializers import AccountSerializer
# Create your views here.


class AccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        card_number = self.request.GET.get('card_number', None)
        if card_number:
            return Account.objects.all().filter(card_number__contains=card_number)
        else:
            return Account.objects.all()
