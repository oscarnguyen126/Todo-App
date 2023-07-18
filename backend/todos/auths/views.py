import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def login_view(request):
    data = json.loads(request.body)

    username = data["username"]
    password = data["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse(json.dumps({"current_user_id": user.id}))
    else:
        return JsonResponse({"msg": "Invalid username or password"})


@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponse(json.dumps({"msg": "Logout successful"}))
