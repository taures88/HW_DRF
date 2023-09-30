from django.urls import path

from studies.apps import StudiesConfig
from rest_framework.routers import DefaultRouter

from studies.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentListAPIView, SubscriptionCreateAPIView, \
    SubscriptionDestroyAPIView, PaymentDeleteAPIView, PaymentCreateAPIView, PaymentUpdateAPIView, PaymentDetailAPIView

app_name = StudiesConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'), # создание уроков
                  path('lesson/', LessonListAPIView.as_view(), name='lesson-list'), # список уроков
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'), # информация по уроку
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'), # редактор уроков
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'), # удаление уроков

                  path('payment/', PaymentListAPIView.as_view(), name='payment-list'), # список оплат
                  path('payment/<int:pk>/', PaymentDetailAPIView.as_view(), name='payment-detail'),# информация об определенной оплате
                  path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment-update'),# обновление
                  path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),# создание платежа
                  path('payment/delete/<int:pk>/', PaymentDeleteAPIView.as_view(), name='payment-delete'),# удаление платежа

                  path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription-create'),
                  path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(),
                       name='subscription-delete'),

              ] + router.urls
