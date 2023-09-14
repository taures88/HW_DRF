from django.db.models import Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, generics

from studies.models import Course, Lesson
from studies.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer, CourseListSerializer, \
    LessonDetailSerializer


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


