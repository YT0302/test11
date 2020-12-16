from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from course.models import CourseCategory, Course, CourseChapter, CourseLesson
from course.pagination import CoursePageNumberPagination

from course.serializer import CourseCategoryModelSerializer, CourseModelSerializer, CoursedetailModelSerializer, \
    CourseChapterModelSerializer, CourseLessonModelSerializer


class CourseCategoryAPIView(ListAPIView):
    """课程分类查询"""
    queryset = CourseCategory.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseCategoryModelSerializer


class CourseAPIView(ListAPIView):
    """课程列表"""
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseModelSerializer

    # 根据点击的分类的id不同来展示对应课程
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ("course_category",)

    # 分页器
    pagination_class = CoursePageNumberPagination



# class CourseFilterAPIView(ListAPIView):
#     # 有条件的查询课程（如点击分类，查询分类下的课程）
#     queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders")
#     serializer_class = CourseModelSerializer
#
#     # 根据点击的分类的id不同来展示对应课程
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     filter_fields = ("course_category",)
#
#     # 排序?????????????????????????????????????????????????????????????????????????
#     ordering_fields = ("id", "students", "price")
#
#     # 分页的实现
#     pagination_class = CoursePageNumberPagination


class CoursedetailAPIView(RetrieveAPIView):
    # 查询单个课程的详细信息
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CoursedetailModelSerializer


class CourseChapterAPIView(ListAPIView):
    # 查询课程章节
    queryset = CourseChapter.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseChapterModelSerializer


class CourseLessonAPIView(ListAPIView):
    # 查询课程课时
    queryset = CourseLesson.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseLessonModelSerializer




