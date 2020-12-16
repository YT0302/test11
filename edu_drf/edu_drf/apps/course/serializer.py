from rest_framework.serializers import ModelSerializer

from course.models import CourseCategory, Course, Teacher, CourseChapter, CourseLesson


class CourseCategoryModelSerializer(ModelSerializer):
    # 课程分类
    class Meta:
        model = CourseCategory
        fields = ('id', 'name')


class TeacherModelSerializer(ModelSerializer):
    """讲师"""
    class Meta:
        model = Teacher
        fields = ("id", "name", "title", "signature", "image", "brief")


class CourseModelSerializer(ModelSerializer):
    # 课程
    teacher = TeacherModelSerializer()
    class Meta:
        model = Course
        fields = ("id", "name", "course_img", "students", "lessons", "pub_lessons",
                  "price", "teacher", "show_lesson_list")


# 单个课程详细信息的序列化器
class CoursedetailModelSerializer(ModelSerializer):

    teacher = TeacherModelSerializer()

    class Meta:
        model = Course
        fields = ("id", "name", "course_img", "students", "lessons", "pub_lessons",
                  "price", "teacher", "level_zh", 'brief_html')


# 定义课程章节的序列化器
class CourseChapterModelSerializer(ModelSerializer):
    """课程章节"""
    class Meta:
        model = CourseChapter
        fields = ('course', 'chapter', 'name')


# 定义课程课时的序列化器
class CourseLessonModelSerializer(ModelSerializer):
    """课程章节"""
    class Meta:
        model = CourseLesson
        fields = ('name', 'course', 'chapter', 'duration', 'free_trail')