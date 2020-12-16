from django.urls import path

from course import views

urlpatterns=[
    # 课程分类
    path('category/',views.CourseCategoryAPIView.as_view()),
    path('courses/',views.CourseAPIView.as_view()),
    path('coursedetail/<int:pk>/',views.CoursedetailAPIView.as_view()),
    path('coursechapter/',views.CourseChapterAPIView.as_view()),
    path('courselesson/',views.CourseLessonAPIView.as_view()),
]