from django.db.models import Count
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, generics
from django_filters.rest_framework import DjangoFilterBackend
from studies.models import Course, Lesson, Payment
from studies.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer, CourseListSerializer, \
    LessonDetailSerializer, PaymentListSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.annotate(lessons_count=Count('lesson'))
    default_serializer = CourseSerializer
    serializers = {
        'list': CourseListSerializer,
        'retrieve': CourseDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

"""
    создание урока
"""
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

"""
    просмотр всех уроков
"""
class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

"""
    просмотр одного урока
"""
class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonDetailSerializer
    queryset = Lesson.objects.all()

"""
    изменение(обновление) урока
"""
class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


"""
    удаление урока
"""
class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()

"""выводит фильтры"""
class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentListSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ('date_payment',)


