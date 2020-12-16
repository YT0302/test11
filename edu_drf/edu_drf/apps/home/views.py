from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from home.models import Banner, Nav
from home.serializers import BannerModelSerializer, NavModelSerializer

# 轮播图的类视图
class BannerAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_delete=False, is_show= True).order_by('-orders')
    serializer_class = BannerModelSerializer

# 导航栏的类视图
class NavAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_delete=False, is_show= True).order_by('orders')
    serializer_class = NavModelSerializer