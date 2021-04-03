from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView
from .models import Account
from .serializers import AccountSerializer
# Create your views here.


class AccountView(APIView, CreateModelMixin):
    serializer_class = AccountSerializer

    def get(self, request):
        accounts = Account.objects.all()
        card_number = request.GET.get("card_number",None)
        if card_number:
            accounts = Account.objects.all().filter(card_number__contains=card_number)
            serializer = AccountSerializer(accounts, many=True)
            return Response({"Account":serializer.data})
        else:
            serializer = AccountSerializer(accounts,many=True)
            return Response({"Accounts": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request):
        return self.create(request)

