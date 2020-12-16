from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserInfo(AbstractUser):
    phone = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True, verbose_name='用户头像')

    class Meta:
        db_table = 'edu_user'
        verbose_name = '用户',
        verbose_name_plural =verbose_name