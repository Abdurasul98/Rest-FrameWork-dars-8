from app1.models.auth_user import *


# class Course(BaseModel):
#     title = models.CharField(max_length=50)
#     descriptions = models.CharField(max_length=500,blank=True,null=True)
#
#
#     def __str__(self):
#         return self.title
#
#
# class Departments(BaseModel):
#     title= models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)
#     description = models.CharField(max_length=300,blank=True,null=True)
#
#
#     def __str__(self):
#         return self.title


class Teacher(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user')
    # departments = models.ManyToManyField(Departments,related_name='get_department')
    # course = models.ManyToManyField(Course,related_name='get_course')
    descriptions = models.CharField(max_length=500,blank=True,null=True)


    def __str__(self):
        return self.user.phone_number