from django.urls import path
from auths import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view),
]