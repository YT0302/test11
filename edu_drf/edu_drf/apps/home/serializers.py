from rest_framework.serializers import ModelSerializer

from home.models import Banner, Nav


class BannerModelSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = ['title', 'link', 'img', 'is_show']


class NavModelSerializer(ModelSerializer):
    class Meta:
        model = Nav
        fields = ['title', 'link', 'is_show', 'is_site', 'is_position']
