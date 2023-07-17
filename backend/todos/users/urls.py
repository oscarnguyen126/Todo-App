from django.urls import path
from users import views


urlpatterns = [
    path("", views.UserList.as_view()),
    path("<int:pk>", views.UserDetails.as_view()),
]
