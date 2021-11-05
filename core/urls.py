from rest_framework.routers import DefaultRouter

from core import viewsets

router = DefaultRouter()
router.register('zone', viewsets.ZoneViewSet)

urlpatterns = router.urls
