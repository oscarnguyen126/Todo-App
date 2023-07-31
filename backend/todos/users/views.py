from .models import User
from .serializers import UserSerializer, UserListSerializer, UserUpdateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated


class UserList(APIView):
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.request.method == 'POST':
            return []
        return super().get_permissions()

    def get(self, request):
        users = User.objects.all()
        return Response(
            UserListSerializer(users, many=True).data, status = status.HTTP_200_OK
        )

    def post(self, request):
        user = User.objects.filter(username=request.data['username'])
        if len(user):
            return Response({"message": "This username already used!"})

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)


class UserDetails(APIView):
    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk=pk)
        serializer = UserListSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        current_user = request.user
        data = JSONParser().parse(request)
        serializer = UserUpdateSerializer(current_user, data=data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = self.get_object(pk=pk)
        user.delete()
        return Response({"msg": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

