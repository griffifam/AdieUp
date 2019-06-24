from adieup.models import Adie, Company, Offer
from rest_framework import viewsets, permissions
from .serializers import AdieSerializer, CompanySerializer, OfferSerializer


#Adie viewsets

class AdieViewSet(viewsets.ModelViewSet):
    queryset = Adie.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AdieSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CompanySerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OfferSerializer
