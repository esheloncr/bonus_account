from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
from django.urls import path
from .views import RegisterUserMixin, AccountAPIView

app_name = "Account"

router = routers.SimpleRouter()
router.register(r'register', RegisterUserMixin)
router.register(r'accounts', AccountAPIView)

urlpatterns = [
    path("auth/", ObtainAuthToken.as_view()),
] + router.urls
