from app1.models.auth_user import *


class Student(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_line = models.BooleanField(default=False)
    descriptions = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.user.phone_number