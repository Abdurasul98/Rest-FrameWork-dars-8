from django.urls import path
from app1.views.view_teacher import *
from app1.views.view_user import *

urlpatterns = [
    path('teachers/', TeacherView.as_view(),name='teachers'),
    path('create_teacher/',CreateUserView.as_view(),name='create_teacher'),
    path('get_users_teacher',UserView.as_view(),name='get_users_teacher'),
]