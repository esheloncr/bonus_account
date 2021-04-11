from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from .views import AccountViewSet, TransactionViewSet

app_name = "Account"

router = routers.SimpleRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path(r'auth/', auth_views.obtain_auth_token),
] + router.urls
