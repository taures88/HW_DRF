from datetime import timedelta
from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail
from config import settings
from studies.models import Course, Subscription
from users.models import User



@shared_task
def send_mail_about_update(course_id):
    course = Course.objects.get(id=course_id)
    subscriptions = Subscription.objects.filter(status=True, course=course)

    if course.updated_at > timezone.now() - timedelta(hours=4):
        for subscription in subscriptions:
            subject = f'Обновление курса {course.title}'
            message = 'Появилось обновление курса!!!'
            from_email = settings.EMAIL_HOST_USER
            list_of_recipient = [subscription.user.email]

            send_mail(subject,
                      message,
                      from_email,
                      list_of_recipient

                      )


@shared_task
def check_user():
    date_now = timezone.now()
    month_ago = date_now - timedelta(days=30)
    unconnected_user = User.objects.filter(last_login__lt=month_ago)
    unconnected_user.update(is_active=False)