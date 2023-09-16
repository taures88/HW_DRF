from django.urls import path

from studies.apps import StudiesConfig
from rest_framework.routers import DefaultRouter

from studies.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentListAPIView

app_name = StudiesConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'), # создание уроков
                  path('lesson/', LessonListAPIView.as_view(), name='lesson-list'), # список уроков
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'), # информация по уроку
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'), # редактор уроков
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'), # удаление уроков

                  path('payment/', PaymentListAPIView.as_view(), name='payment_list'), # список оплат

              ] + router.urls
