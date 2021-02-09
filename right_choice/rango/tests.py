from django.test import TestCase
from rango.models import University

# Create your tests here.

class UniversityAddTest(TestCase):

    def setUp(self):
        University.objects.create(name="Uni 1", location="loc1",details="details",universityImage=None,slug="1uni1",linkToUniWebsite="www.uni1.com")

    def test_uni_create(self):
        uni1 = University.objects.get(name="Uni 1")
        self.assertEqual(uni1.name, "Uni 1")

