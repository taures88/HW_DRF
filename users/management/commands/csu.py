from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='taures_88@mail.ru',
            first_name='Anton',
            last_name='Turchenko',
            role='moderator',
            is_superuser=True,
            is_staff=True,
            is_active=True

        )

        user.set_password('Fynjybj88')
        user.save()