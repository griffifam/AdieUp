from rest_framework import routers
from .api import AdieViewSet, CompanyViewSet, OfferViewSet

router = routers.DefaultRouter()
router.register('api/adies', AdieViewSet, 'adies')

urlpatterns = router.urls 
