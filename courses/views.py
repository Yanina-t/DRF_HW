from rest_framework import generics, viewsets
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


# Представления для курсов

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseCreateAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDestroyAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# Представления для уроков
class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
