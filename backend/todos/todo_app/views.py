from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from datetime import date


@csrf_exempt
def todo_list(request):
    todos = Todo.objects.all()

    if request.method == 'GET':
        for todo in todos:
            if todo.complete_date < date.today():
                todo.is_expired = True
        serializer = TodoListSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)

        if serializer.is_valid():
            check_list = Todo.objects.filter(complete_date = data['complete_date'], description = data['description'])
            if len(check_list):
                return JsonResponse(serializer.errors, status=400)

            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        todo.delete()
        return HttpResponse(status=204)
