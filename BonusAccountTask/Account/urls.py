from django.urls import path
from rest_framework import routers

from .views import AccountViewSet, TransactionViewSet

app_name = "Account"

router = routers.SimpleRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [] + router.urls