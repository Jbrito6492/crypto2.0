from rest_framework import routers
from .api import CryptoViewSet


router = routers.DefaultRouter()
router.register('api/crypto', CryptoViewSet, 'crypto')

urlpatterns = router.urls
