from rest_framework.routers import DefaultRouter
from .api import AdieViewSet, CompanyViewSet, OfferViewSet

router = DefaultRouter()
router.register(r'api/adies', AdieViewSet, basename='adieup')
router.register(r'api/companies', CompanyViewSet, basename='adieup')
router.register(r'api/offers', OfferViewSet, basename='adieup')


urlpatterns = router.urls
