from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app1.models.auth_user import *
from app1.serializers import UserSerializer


class UserView(APIView):
    def get(self, request):
        teachers = User.objects.all()
        serializer = UserSerializer(teachers, many=True)
        return Response(data= serializer.data,status=status.HTTP_200_OK)