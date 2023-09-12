from rest_framework.viewsets import ModelViewSet, generics

from studies.models import Course, Lesson
from studies.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

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
    serializer_class = LessonSerializer
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


