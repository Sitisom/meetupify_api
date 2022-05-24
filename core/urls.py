from rest_framework.routers import DefaultRouter

from core.views import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet)


urlpatterns = router.urls
