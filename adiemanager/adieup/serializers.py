from rest_framework import serializers
from adieup.models import Adie, Company, Offer

class AdieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adie
        fields = '__all__'
        read_only_fields = ['created_at']

class CompanySerializer(serializers.ModelSerializer):
        class Meta:
            model = Company
            fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
        class Meta:
            model = Offer
            fields = '__all__'
            read_only_fields = ['created_at']
