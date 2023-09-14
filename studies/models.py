from django.db import models

from users.models import User

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
    course_lesson = models.ForeignKey(Course, **NULLABLE, on_delete=models.CASCADE, verbose_name='Урок курса')


    def __str__(self):
        return f'{self.title} {self.link}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'



class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_payment = models.DateField(verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченный урок')
    payment_amount = models.PositiveIntegerField('Сумма оплаты')
    payment_method = models.CharField(max_length=150, **NULLABLE, verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.user}: {self.paid_course} - {self.payment_amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'