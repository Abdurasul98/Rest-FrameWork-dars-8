from rest_framework import serializers
from app1.models.model_teacher import *
from app1.models.model_student import *
from app1.models.auth_user import *



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number','email','password']
        extra_kwargs = {'password': {'write_only': True}}



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username']
        fields = '__all__'

# class DepartmentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Departments
#         fields = '__all__'


# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = '__all__'