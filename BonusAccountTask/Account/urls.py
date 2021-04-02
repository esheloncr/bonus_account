from django.urls import path
from .views import AccountView

app_name = "Accounts"

urlpatterns = [
    path("Accounts", AccountView.as_view())
]