from rest_framework import serializers

"""класс валидатор на проверку ссылки видео только с сайта YouTube"""


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('link'):
            if 'www.youtube.com' not in value.get('link'):
                raise serializers.ValidationError('Ссылки на сторонние ресурсы запрещены, кроме YouTube')