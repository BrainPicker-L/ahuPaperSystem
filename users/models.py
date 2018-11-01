from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    user_name = models.CharField('姓名', max_length=128, blank=True, default='未知')

    stu_id = models.CharField('学号', max_length=128, blank=True)

    major = models.CharField('院系', max_length=50, blank=True)


class Meta:
    verbose_name = 'User Profile'

def __str__(self):
    return self.user.__str__()
