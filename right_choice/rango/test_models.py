from django.test import TestCase
from rango.models import *
from django.utils import timezone
from django.http import HttpResponse
from django.urls import reverse
from rango import views

# Models test

class UniversityAddTest(TestCase):

    def setUp(self):
        return University.objects.get_or_create(name="Uni 1", location="loc1",details="details",universityImage=None,slug="1uni1",linkToUniWebsite="www.uni1.com")

    def test_uni_create(self):
        uni1 = University.objects.get(name="Uni 1")
        self.assertEqual(uni1.name, "Uni 1")
    
    def test_uni_str(self):
        uni1 = University.objects.get(name="Uni 1")
        self.assertEqual(str(uni1), "Uni 1")

class CollegeAddTest(TestCase):

    def setUp(self):
        return College.objects.get_or_create(name="College 1", location="loc1",details="details",collegeImage=None,slug="1college1",linkToCollegeWebsite="www.college1.com")

    def test_college_create(self):
        College1 = College.objects.get(name="College 1")
        self.assertEqual(College1.name, "College 1")
    
    def test_college_str(self):
        college1 = College.objects.get(name="College 1")
        self.assertEqual(str(college1), "College 1")

class CompanyAddTest(TestCase):

    def setUp(self):
        return Company.objects.get_or_create(name="Company 1", location="loc1",details="details",companyImage=None,slug="1company1",linkToCompanyWebsite="www.company1.com")

    def test_company_create(self):
        company1 = Company.objects.get(name="Company 1")
        self.assertEqual(company1.name, "Company 1")
    
    def test_company_str(self):
        company1 = Company.objects.get(name="Company 1")
        self.assertEqual(str(company1), "Company 1")

class ApprenticeshipAddTest(TestCase):

    def setUp(self):
        return Apprenticeship.objects.get_or_create(name="App 1", location="loc1",details="details",companyImage=None,slug="1company1",linkToCompanyWebsite="www.company_app1.com")

    def test_apprenticeship_create(self):
        app1 = Apprenticeship.objects.get(name="App 1")
        self.assertEqual(app1.name, "App 1")
    
    def test_apprenticeship_str(self):
        app1 = Apprenticeship.objects.get(name="App 1")
        self.assertEqual(str(app1), "App 1")

class CareerAddTest(TestCase):

    def setUp(self):
        return Career.objects.get_or_create(careerName="Career 1", areaStudy="Area of study")

    def test_career_create(self):
        career1 = Career.objects.get(careerName="Career 1")
        self.assertEqual(career1.careerName, "Career 1")
    
    def test_career_str(self):
        career1 = Career.objects.get(careerName="Career 1")
        self.assertEqual(str(career1), "Career 1")

class SchoolSubTEst(TestCase):

    def setUp(self):
        career = Career.objects.get_or_create(careerName="Career 1")[0]
        s = SchoolSubjects.objects.get_or_create(name="Subject 1", level="Higher", subjectArea="Sub Area")[0]
        
        return s

    def test_subject_create(self):
        subject1 = SchoolSubjects.objects.get(name="Subject 1")
        self.assertEqual(subject1.name, "Subject 1")
    
    def test_subject_str(self):
        subject1 = SchoolSubjects.objects.get(name="Subject 1")
        self.assertEqual(str(subject1), "Subject 1")