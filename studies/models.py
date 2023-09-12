from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}

NOT_NULLABLE = {
    'null': False,
    'blank': False
}

class Course(models.Model):
    title = models.CharField(max_length=35, verbose_name='Название')
    preview = models.ImageField(upload_to='courses', verbose_name='Изображение', **NULLABLE)
    desc = models.TextField(max_length=250, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=35, verbose_name='Название')
    desc = models.TextField(max_length=250, verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(upload_to='courses', verbose_name='Изображение', **NULLABLE)
    link = models.URLField(verbose_name='ссылка на видео', **NULLABLE)


    def __str__(self):
        return f'{self.title} {self.link}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'