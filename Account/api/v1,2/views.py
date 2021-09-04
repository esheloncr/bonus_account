from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import JsonResponse
from Account.models import Account
from .serializers import AccountSerializer, UserRegistrationSerializer
from .schemas import AccountsSchema


class AccountAPIView(APIView):
    """
    View for get list of active accounts, filter by card number and create a new account
    """
    def get_queryset(self):
        return Account.objects.filter(is_active=True)

    def get_serializer_class(self):
        return AccountSerializer

    def get(self, request):
        serializer = self.get_serializer_class()
        serializer = serializer(self.get_queryset(), many=True)
        return JsonResponse({"Accounts": serializer.data})

    def post(self, request):
        cn = request.data.get("card_number")
        queryset = self.get_queryset()
        query = queryset.filter(card_number=cn)
        serializer = self.get_serializer_class()
        if not query.exists():
            return JsonResponse({"message": "Can`t find account by given card number"})
        if not query.first().is_active:
            return JsonResponse({"message": "Account pending verification"})
        serializer = serializer(query, many=True)
        return JsonResponse({"Account": serializer.data})

    @action(detail=False, methods=["POST"], url_path="create")
    def create_account(self, request):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"message": "Success created"}, status=status.HTTP_201_CREATED)


class RegisterUserMixin(CreateModelMixin, GenericViewSet):
    """
    View for register a user to access to token
    """
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return JsonResponse({"message": "Success register"}, status=status.HTTP_201_CREATED)


# class AccountViewSet(ListModelMixin, GenericViewSet):
#     serializer_class = AccountSerializer
#     queryset = Account.objects.filter(is_active=True)
#     permission_classes = [IsAuthenticated]
#
#     @action(detail=False, methods=["POST"], schema=AccountsSchema(), url_path="../accounts")
#     def filter_by_card_name(self, request):
#         """
#         Search a user by card number.
#         """
#         cn = request.data.get("card_number")
#         account = self.queryset.filter(card_number=cn)
#         if account.exists():
#             if not account.first().is_active:
#                 return JsonResponse({"message": "Account pending verification"})
#             serializer = self.serializer_class(account, many=True)
#             return JsonResponse({"account": serializer.data})
#         return JsonResponse({"message": "Can`t find account by given card number"})
#
#     @action(detail=False, methods=["POST"], url_path="create")
#     def create_account(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return JsonResponse({"message": "Success created"}, status=status.HTTP_201_CREATED)