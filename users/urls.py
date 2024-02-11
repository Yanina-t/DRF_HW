from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserViewSet

app_name = 'users'

# Описание маршрутизации для ViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls
