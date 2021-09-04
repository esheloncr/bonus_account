from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from django.urls import path
from .views import RegisterUserMixin, AccountAPIView

app_name = "Account"

router = routers.SimpleRouter()
router.register(r'register', RegisterUserMixin)

urlpatterns = [
    path("auth/", auth_views.obtain_auth_token),
    path(r"accounts/", AccountAPIView.as_view())
] + router.urls
