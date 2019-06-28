from rest_framework.test import APITestCase
from adieup.models import Adie, Company, Offer
from rest_framework import status

# automated
# new / blank db

class AdieAPITestCase(APITestCase):
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
        adie2 = Adie.objects.create(
            age=25,
            gender='non-binary',
            race='latinx',
            orientation='queer',
            transplant=False,
            city='seattle',
            state='washington'
            )

    def test_adie_string_representation(self):
                adie = Adie.objects.all()[:1].get()
                self.assertEqual(str(adie), 'Adie ID: 3')

    def test_adie_info(self):
                female_adie_count = Adie.objects.filter(gender='female').count()
                self.assertEqual(female_adie_count, 1)

    def test_create_new_adie(self):
        count = Adie.objects.all().count()
        adie = Adie.objects.create(
            age=32,
            gender='non-binary',
            race='latinx',
            orientation='queer',
            transplant=False,
            city='seattle',
            state='washington'
        )
        self.assertEqual(count + 1, Adie.objects.all().count())

    # def test_return_adie_data(self):
    #   adie = adie =  Adie.objects.all()[:1].get()
    # Can I return the correct data from an Adie
    # Can I return an instance of Adie
    # Can I update an instance of Adie
    # Can I delete an instance of Adie

class CompanyAPITestCase(APITestCase):
    def setUp(self):
        company = Company.objects.create(
            startup=True,
            org_size=10,
            city='chicago',
            state='illinois',
            industry='real estate',
            adies_present=False
        )
        def test_company_string_representation(self):
            company = Company.objects.all()[:1].get()
            self.assertEqual(str(company), 'Industry: real estate - chicago,  illinois')

        def test_company_count(self):
            company_count = Company.objects.count()
            self.assertEqual(company_count, 1)

        def test_company_info(self):
            org_size_greater_than_ten = Company.objects.filter(org_size__gte=5).count()
            self.assertEqual(org_size_greater_than_ten, 1)

    # def createNewCompany(self):
    # # Can I create an instance of a Company
    # # Can I return the correct data from a Company
    # # Can I return an instance of a Company
    # # Can I update an instance of a Company
    # # Can I delete an instance of a Company

class OfferAPITestCase(APITestCase):
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

        company1 = Company.objects.create(
            startup=True,
            org_size=10,
            city='chicago',
            state='illinois',
            industry='real estate',
            adies_present=False
        )

        offer = Offer.objects.create(
            adie = adie1,
            company = company1,
            base_amount=100000,
            signing_bonus=22000,
            negotiations=True,
            relocation_package=True,
            health_insurance=True,
            retirement_matching=60,
            vacation_days=24,
        )

    def test_offer_string_representation(self):
        offer = Offer.objects.all()[:1].get()
        self.assertEqual(str(offer), 'Adie: 9,\nCompany: 2,\nBase Pay: 100000')

    def test_offer_info(self):
        adie1 = Adie.objects.all()[:1].get()
        company1 = Company.objects.all()[:1].get()
        offer = Offer.objects.all()[:1].get()
        self.assertEqual(offer.adie, adie1)
        self.assertEqual(offer.company, company1)

    # def createNewOffer(self):
    # Can I create an instance of an Offer
    # Can I return the correct data from an Offer
    # Can I return an instance of an Offer
    # Can I update an instance of an Offer
    # Can I delete an instance of an Offer
