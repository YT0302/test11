from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from user.models import UserInfo

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token':token,
        'username':user.username,
        'user_id':user.id
    }


class UserAuthentication(ModelBackend):
    # 重写认证
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 根据用户名（账号）获取用户对象
        user = UserInfo.objects.filter(Q(username=username ) | Q(phone=username) | Q(email=username)).first()
        print(user)
        # 判断用户是否存在
        if user:
            # 判断密码是否正确
            if user.check_password(password) and user.is_authenticated:
                return user
        return None