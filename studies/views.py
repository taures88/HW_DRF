from django.db.models import Count
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, generics
from django_filters.rest_framework import DjangoFilterBackend
from studies.models import Course, Lesson, Payment
from studies.paginators import StudiesPaginator
from studies.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer, CourseListSerializer, \
    LessonDetailSerializer, PaymentListSerializer, SubscriptionSerializer, PaymentRetrieveSerializer, \
    PaymentCreateSerializer, PaymentSerializer
from users.permissions import IsBuyer, IsModerator


class CourseViewSet(ModelViewSet):
    serializer_class = CourseDetailSerializer
    permission_classes = [IsAuthenticated, IsBuyer | IsModerator]
    queryset = Course.objects.annotate(lessons_count=Count('lesson'))
    default_serializer = CourseSerializer
    pagination_class = StudiesPaginator
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
    permission_classes = [IsAuthenticated]


"""
    просмотр всех уроков
"""


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = StudiesPaginator
    permission_classes = [IsAuthenticated]


"""
    просмотр одного урока
"""


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonDetailSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsBuyer | IsModerator]


"""
    изменение(обновление) урока
"""


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsBuyer | IsModerator]


"""
    удаление урока
"""


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsBuyer | IsModerator]


"""выводит оплаты"""


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentListSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ('date_payment',)
    permission_classes = [IsAuthenticated]
    pagination_class = StudiesPaginator


"""детализация конкретного платежа"""


class PaymentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentRetrieveSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


"""создание платежа"""


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentCreateSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated, IsBuyer, IsModerator]


"""обновление платежа"""


class PaymentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


"""удаление платежа"""


class PaymentDeleteAPIView(generics.DestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


"""создание подписки"""


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Lesson.objects.all()


"""удаление подписки"""


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Lesson.objects.all()
