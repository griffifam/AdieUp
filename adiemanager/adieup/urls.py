from rest_framework import routers
from .api import AdieViewSet, CompanyViewSet, OfferViewSet

router = routers.DefaultRouter()
router.register('api/adies', AdieViewSet, 'adies')
router.register('api/companies', CompanyViewSet, 'companies')
router.register('api/offers', OfferViewSet, 'offers')


urlpatterns = router.urls
