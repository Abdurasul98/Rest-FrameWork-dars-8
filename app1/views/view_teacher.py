from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from app1.serializers import *
from rest_framework.response import Response


class TeacherView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(data= serializer.data,status=status.HTTP_200_OK)


    @swagger_auto_schema(request_body=StudentSerializer)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student_user = serializer.validated_data['user']
            student_user.is_student = True
            student_user.save()
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(APIView):
    @swagger_auto_schema(request_body=CreateUserSerializer)
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user = User.objects.create(
                phone_number = data['phone_number'],
                email = data['email'],
                is_teacher=True,
                is_staff=True,
                is_superuser=True,
            )
            user.set_password(data['password'])
            user.save()
            Teacher.objects.create(user=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)