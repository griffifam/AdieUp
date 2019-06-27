from rest_framework import routers
from rest_framework import status
from rest_framework.test import APIRequestFactory
import pdb


class AdieAPIRequestFactory(APIRequestFactory):
    def test_adie_get(self):
        factory = APIRequestFactory()
        request = factory.get('/api/adies')
        pdb.set_trace()
