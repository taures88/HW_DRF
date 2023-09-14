from rest_framework import serializers
from rest_framework.fields import IntegerField, SerializerMethodField
from rest_framework.relations import SlugRelatedField

from studies.models import Course, Lesson, Payment
from users.models import User


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    lessons_count = IntegerField()

    class Meta:
        model = Course
        fields = ('pk', 'title', 'desc', 'lessons_count')


class CourseDetailSerializer(serializers.ModelSerializer):
    the_course_lessons = SerializerMethodField()

    def get_the_course_lessons(self, course):
        return [lesson.title for lesson in Lesson.objects.filter(course_lesson=course)]

    class Meta:
        model = Course
        fields = ('pk', 'title', 'preview', 'desc', 'the_course_lessons')

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'



class LessonDetailSerializer(serializers.ModelSerializer):
    course_lesson = CourseDetailSerializer
    count_lesson_with_course = SerializerMethodField()

    def get_count_lesson_with_course(self, lesson):
        return Lesson.objects.filter(course_lesson=lesson.course_lesson).count()

    class Meta:
        model = Lesson
        fields = ('pk', 'title', 'preview', 'desc', 'link', 'course_lesson', 'count_lesson_with_course')



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentListSerializer(serializers.ModelSerializer):
    paid_course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    paid_lesson = SlugRelatedField(slug_field='title', queryset=Lesson.objects.all())

    class Meta:
        model = Payment
        fields = ('pk', 'user', 'date_payment', 'paid_course', 'paid_lesson', 'payment_amount', 'payment_method')


