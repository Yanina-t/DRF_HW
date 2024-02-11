from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, **NULLABLE)
    preview = models.ImageField(upload_to='course_previews/', **NULLABLE)
    description = models.TextField(**NULLABLE)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=100, **NULLABLE)
    description = models.TextField(**NULLABLE)
    preview = models.ImageField(upload_to='lesson_previews/',**NULLABLE)
    video_link = models.URLField()
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
