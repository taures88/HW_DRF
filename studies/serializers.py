from rest_framework import serializers
from rest_framework.fields import IntegerField, SerializerMethodField
from rest_framework.relations import SlugRelatedField

from studies.models import Course, Lesson, Payment, Subscription
from studies.services import retrieve_payment, create_payment, make_payment
from studies.validators import LinkValidator
from users.models import User

"""Класс сериализатор курсов"""


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


"""Класс сериализатор курсов, вывод списка курсов"""


class CourseListSerializer(serializers.ModelSerializer):
    lessons_count = IntegerField()

    class Meta:
        model = Course
        fields = ('pk', 'title', 'desc', 'lessons_count')


"""Класс сериализатор курсов, информация по курсам"""


class CourseDetailSerializer(serializers.ModelSerializer):
    the_course_lessons = SerializerMethodField()

    def get_the_course_lessons(self, course):
        return [lesson.title for lesson in Lesson.objects.filter(course_lesson=course)]

    class Meta:
        model = Course
        fields = ('pk', 'title', 'preview', 'desc', 'the_course_lessons')


"""Класс сериализатор уроков"""


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        validators = [LinkValidator(field='link')]
        fields = '__all__'


"""Класс сериализатор уроков, информация по урокам"""


class LessonDetailSerializer(serializers.ModelSerializer):
    course_lesson = CourseDetailSerializer
    count_lesson_with_course = SerializerMethodField()

    def get_count_lesson_with_course(self, lesson):
        return Lesson.objects.filter(course_lesson=lesson.course_lesson).count()

    class Meta:
        model = Lesson
        validators = [LinkValidator(field='link')]
        fields = ('pk', 'title', 'preview', 'desc', 'link', 'course_lesson', 'count_lesson_with_course')


"""Класс сериализатор оплат"""


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentListSerializer(serializers.ModelSerializer):
    payment_status = serializers.SerializerMethodField()
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    paid_course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    paid_lesson = SlugRelatedField(slug_field='title', queryset=Lesson.objects.all())

    class Meta:
        model = Payment
        fields = ('__all__')

    def get_payment_status(self, instance):
        return retrieve_payment(instance.payment_intent_id)


"""Создание оплаты"""


class PaymentCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['payment_intent_id'] = create_payment(int(validated_data.get('payment_amount')))
        payment = Payment.objects.create(**validated_data)
        return payment

    class Meta:
        model = Payment
        fields = "__all__"


"""Информация об оплате(платеже)"""


class PaymentRetrieveSerializer(serializers.ModelSerializer):
    payment_status = serializers.SerializerMethodField()

    def get_payment_status(self, instance):
        return retrieve_payment(instance.payment_intent_id)

    class Meta:
        model = Payment
        fields = "__all__"


"""Обновление оплаты"""


class PaymentUpdateSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        payment = make_payment(instance.payment_intent_id)
        if payment == 'succeeded':
            instance.is_paid = True
            instance.save()
            return instance
        else:
            return instance

    class Meta:
        model = Payment
        fields = "__all__"


"""Класс сериализатор подписки"""


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
