# Generated by Django 4.2.5 on 2023-09-14 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0002_alter_lesson_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studies.course', verbose_name='Урок курса'),
        ),
    ]
