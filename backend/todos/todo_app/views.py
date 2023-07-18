from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from datetime import date


@csrf_exempt
def todo_list(request):
    if not request.user.is_authenticated:
        return HttpResponse(status=404)


    todos = Todo.objects.filter(user_id=request.user.id)
    if request.method == 'GET':
        for todo in todos:
            if todo.complete_date < date.today():
                todo.is_expired = True
        serializer = TodoListSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False)


    # Creating a new todo of current user
    elif request.method == 'POST':
        current_user = request.user
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)

        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)

        check_list = Todo.objects.filter(complete_date = data['complete_date'], description = data['description'])
        if len(check_list):
            return JsonResponse(serializer.errors, status=400)

        todo = serializer.save()
        todo.user = current_user
        todo.save()
        return JsonResponse(serializer.data, status=201, safe=False)


@csrf_exempt
def todo_detail(request, pk):
    if not request.user.is_authenticated:
        return JsonResponse({"msg":"You're not log in"}, status=404)


    try:
        todo = Todo.objects.get(pk=pk)
        # TODO: move this logic to a middleware
        if request.user.id != todo.user_id:
            return JsonResponse({"msg":"Permission denied"}, status=401)
    except Todo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TodoListSerializer(todo)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(todo, data=data)
        if serializer.is_valid():
            todo = serializer.save()
            todo.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        todo.delete()
        return HttpResponse(status=204)
