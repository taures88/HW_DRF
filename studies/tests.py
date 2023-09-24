from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from studies.models import Course, Lesson
from users.models import User, UserRoles


class LessonCreateTest(APITestCase):

    def setUp(self):
        """Заполнение первичных данных"""

        self.user = get_user_model().objects.create(
            email='taures_88@mail.ru',
            first_name='Anton',
            last_name='Turchenko',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role=UserRoles.moderator,
        )
        self.user.set_password('Fynjybj88')
        self.user.save()

        self.course = Course.objects.create(
            title='Existing Course',
            desc='Existing Description'
        )

    def test_lesson_create(self):
        """Тест для создания уроков"""

        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Test1Lesson',
            'desc': 'Test1Lesson',
            'link': 'https://www.youtube.com/watch?v=abc123',
            'course_lesson': self.course.id,
            'buyer': self.user.id
        }
        response = self.client.post(
            '/lesson/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

class LessonDeleteTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            email='taures_88@mail.ru',
            first_name='Anton',
            last_name='Turchenko',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role=UserRoles.moderator,
        )
        self.user.set_password('Fynjybj88')
        self.user.save()

        self.course = Course.objects.create(
            title='Existing Course',
            desc='Existing Description'
        )

        self.lesson = Lesson.objects.create(
            title='Test1Lesson',
            desc='Test1Lesson',
            link='https://www.youtube.com/watch?v=abc123',
            course_lesson=self.course,
        )

    def test_delete_lesson(self):
        """ Тестирование удаления урока """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            f'/lesson/delete/{self.lesson.id}/',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())


class LessonListViewTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            email='taures_88@mail.ru',
            first_name='Anton',
            last_name='Turchenko',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role=UserRoles.moderator,
        )
        self.user.set_password('Fynjybj88')
        self.user.save()

        self.course = Course.objects.create(
            title='Existing Course',
            desc='Existing Description'
        )

        self.lesson = Lesson.objects.create(
            title='Test1Lesson',
            desc='Test1Lesson',
            link='https://www.youtube.com/watch?v=abc123',
            course_lesson=self.course,
        )

    def test_list_lessons(self):
        """ Тестирование на отображение урока """
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/lesson/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)

        self.assertEqual(len(response.data), 4)


class LessonUpdateTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            email='taures_88@mail.ru',
            first_name='Anton',
            last_name='Turchenko',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role=UserRoles.moderator,
        )
        self.user.set_password('Fynjybj88')
        self.user.save()

        self.course = Course.objects.create(
            title='Existing Course',
            desc='Existing Description'
        )

        self.lesson_data = {
            'title': 'Test1Lesson',
            'desc': 'Test1Lesson',
            'preview': 'https://example.com/preview.jpg',
            'link': 'https://www.youtube.com/watch?v=abc123',
            'course_lesson': self.course,
        }
        self.lesson = Lesson.objects.create(**self.lesson_data)

    def test_update_lesson(self):
        """ Тестирование обновления урока """
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Update Lesson',
            'desc': 'Update lesson',
            'link': 'https://www.youtube.com/watch?v=update45',
            'course_lesson': self.course.id,
        }
        response = self.client.put(
            f'/lesson/update/{self.lesson.id}/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, data['title'])
        self.assertEqual(self.lesson.desc, data['desc'])
        self.assertEqual(self.lesson.link, data['link'])