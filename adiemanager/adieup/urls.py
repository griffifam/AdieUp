from rest_framework.routers import DefaultRouter
from .api import AdieViewSet, CompanyViewSet, OfferViewSet

router = DefaultRouter()
router.register(r'api/adies', AdieViewSet, basename='adies')
router.register(r'api/companies', CompanyViewSet, basename='companies')
router.register(r'api/offers', OfferViewSet, basename='offers')


urlpatterns = router.urls
