from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todo_app.urls')),
    path('users/', include("users.urls")),
    path("auths/", include("auths.urls")),
]
