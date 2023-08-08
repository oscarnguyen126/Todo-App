from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from datetime import date
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

#Todo: Filter BY CONTENT
# check benchmark of the query
# add index to content column then run benchmark again

class TodoList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        todos = Todo.objects.filter(user_id=request.user.id)
        for todo in todos:
            if todo.complete_date < date.today():
                todo.is_expired = True

            if request.GET.get("description"):
                todo = todos.filter(description__icontains=request.GET.get("description"))
                serializer = TodoListSerializer(todo, many=True)
                return JsonResponse(serializer.data, safe=False)
            elif request.GET.get("complete_date"):
                todo = todos.filter(complete_date=request.GET.get("complete_date"))
                serializer = TodoListSerializer(todo, many=True)
                return JsonResponse(serializer.data, safe=False)

        serializer = TodoListSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False)


    def post(self, request):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            check_list = Todo.objects.filter(complete_date = request.data['complete_date'], description = request.data['description'])
            if len(check_list):
                return JsonResponse(serializer.errors, status=400)

            todo = serializer.save()
            todo.user = request.user
            todo.save()
            return JsonResponse(serializer.data, status=201)


class TodoDetail(APIView):
    def get_todo(self, pk):
        return get_object_or_404(Todo, pk=pk)


    def get(self, request, pk):
        todo = self.get_todo(pk=pk)
        serializer = TodoListSerializer(todo)
        return JsonResponse(serializer.data, status=200)


    def put(self, request, pk):
        todo = self.get_todo(pk=pk)
        data = JSONParser().parse(request)
        serializer = TodoSerializer(todo, data=data)
        
        if serializer.is_valid(raise_exception=True):
            todo = serializer.save()
            todo.save()
            return JsonResponse(serializer.data, status=201)


    def delete(self, request, pk):
        todo = self.get_todo(pk=pk)
        todo.delete()
        return JsonResponse({"msg": "Todo removed"}, status=204)
