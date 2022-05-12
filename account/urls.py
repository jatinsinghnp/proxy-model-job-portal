from django.urls import path
from account.views import (
    LoginViewPage,
    SingUpPageView,
    # CopanyRegrastrationView,
    RegrastrationViewCompany,
    LogoutPage,
)

app_name = "accounts"
urlpatterns = [
    path("login/", LoginViewPage.as_view(), name="log_in"),
    path("register/", SingUpPageView.as_view(), name="sing_in"),
    path("company/", RegrastrationViewCompany.as_view(), name="company"),
    path("logout/", LogoutPage.as_view(), name="logout"),
]
