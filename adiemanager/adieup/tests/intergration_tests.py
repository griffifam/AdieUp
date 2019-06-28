from rest_framework import routers, status
from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase, APIClient
from adieup.api import AdieViewSet, CompanyViewSet, OfferViewSet
from adieup.models import Adie, Company, Offer
import pdb


class AdieAPIRequestFactory(APITestCase):
    def setUp(self):
        adie1 = Adie.objects.create(
            age=30,
            gender='female',
            race='black',
            orientation='straight',
            transplant=True,
            city='seattle',
            state='washington'
            )
    #
    # def test_get_adie_list(self):
    #     request = APIRequestFactory.get(reverse('/api/adies/'))
    #     adie_list = AdieViewSet.as_view({'get': 'retrieve'})
    #     response = self.client.get(self.adie_list, format='json')
    #     # self.assertEqual(response.status_code, 200)
        # response = self.client.get(self.fetch_url, format='json', **auth_headers)
        # Make assertions
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        #     pdb.set_trace()
