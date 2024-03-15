from django.db import models
from django.utils import timezone
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='course_previews/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    price = models.IntegerField(default=0, verbose_name='стоимость курса')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='последнее обновление')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lesson_previews/', verbose_name='превью', **NULLABLE)
    video_link = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    price = models.IntegerField(default=0, verbose_name='стоимость урока')
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='последнее обновление')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


# Подписка
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
