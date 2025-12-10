from django.contrib import admin
from app1.models.model_teacher import *
from app1.models.model_student import Student
from app1.models.auth_user import *

admin.site.register([User,Teacher,Student])