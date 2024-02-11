from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (CourseListCreateAPIView, CourseRetrieveAPIView, CourseCreateAPIView,
                    CourseUpdateAPIView, CourseDestroyAPIView,
                    LessonListCreateAPIView, LessonRetrieveAPIView, LessonCreateAPIView,
                    LessonUpdateAPIView, LessonDestroyAPIView, CourseViewSet)

app_name = 'courses'

# Создаем маршрутизатор
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    # URL-маршруты для курсов
    path('courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveAPIView.as_view(), name='course-retrieve'),
    path('courses/create/', CourseCreateAPIView.as_view(), name='course-create'),
    path('courses/<int:pk>/update/', CourseUpdateAPIView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', CourseDestroyAPIView.as_view(), name='course-delete'),

    # URL-маршруты для уроков
    path('lessons/', LessonListCreateAPIView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
]

# Добавляем URL-маршруты из маршрутизатора
urlpatterns += router.urls
