from rest_framework.serializers import ModelSerializer

from user.models import UserInfo


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['username', 'password', 'phone', 'email']