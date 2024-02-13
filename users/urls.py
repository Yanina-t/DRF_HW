from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentViewSet

app_name = 'users'

# Описание маршрутизации для ViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = router.urls
