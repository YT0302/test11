from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from user import views

urlpatterns =[
    # 登录请求，完成token校验
    path('login/', obtain_jwt_token)
]