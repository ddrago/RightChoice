from django.test import TestCase, Client
from rango.models import *

class ViewsTestCase(TestCase):
    def setUp(self):
        
        self.client = Client()

    def test_index_loads_properly(self):
        """Homepage loads"""
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

    def test_about_loads_properly(self):
        """About page loads"""
        response = self.client.get('http://127.0.0.1:8000/rightchoice/about/')
        self.assertEqual(response.status_code, 200)

    def test_search_results(self):
        """Search page loads"""
        response = self.client.get('http://127.0.0.1:8000/rightchoice/searchResults/')
        self.assertEqual(response.status_code, 200)

    def test_univeristy_loads_properly(self):
        """University page loads"""
        response = self.client.get('http://127.0.0.1:8000/rightchoice/universities/')
        self.assertEqual(response.status_code, 200)
    
    def test_colleges_loads_properly(self):
        """Colleges page loads"""
        response = self.client.get('http://127.0.0.1:8000/rightchoice/colleges/')
        self.assertEqual(response.status_code, 200)
    
    def test_apprenticeships_loads_properly(self):
        """Apprenticeships page loads"""
        response = self.client.get('http://127.0.0.1:8000/rightchoice/apprenticeships/')
        self.assertEqual(response.status_code, 200)


    def test_uni_slug_loads(self):
        """Uni slug page loads"""
        uni = University.objects.get_or_create(name="Uni 1", location="loc1",details="details",universityImage=None,slug="1uni1",linkToUniWebsite="www.uni1.com")[0]
        slug = uni.slug
        response = self.client.get('http://127.0.0.1:8000/rightchoice/university/'+slug+'/')
        self.assertEqual(response.status_code, 200)

    def test__uni_search_results(self):
        """Search page loads"""
        response = self.client.get('http://127.0.0.1:8000/rightchoice/universities/searchResultsUniversities')
        self.assertEqual(response.status_code, 200)
    
    def test__college_search_results(self):
        """Search page loads"""
        response = self.client.get('http://127.0.0.1:8000/rightchoice/universities/searchResultsColleges')
        self.assertEqual(response.status_code, 200)

    def test_uni__search_slug_loads(self):
        """Uni search slug page loads"""
        uni = University.objects.get_or_create(name="Uni 1", location="loc1",details="details",universityImage=None,slug="1uni1",linkToUniWebsite="www.uni1.com")[0]
        slug = uni.slug
        response = self.client.get('http://127.0.0.1:8000/rightchoice/university/searchResults/'+slug+'/')
        self.assertEqual(response.status_code, 200)

    def test_college_slug_loads(self):
        """College slug page loads"""
        college = College.objects.get_or_create(name="College 1", location="loc1",details="details",collegeImage=None,slug="1college1",linkToCollegeWebsite="www.college1.com")[0]
        slug = college.slug
        response = self.client.get('http://127.0.0.1:8000/rightchoice/college/'+slug+'/')
        self.assertEqual(response.status_code, 200)

    def test_college_slug_loads(self):
        """College slug page loads"""
        college = College.objects.get_or_create(name="College 1", location="loc1",details="details",collegeImage=None,slug="1college1",linkToCollegeWebsite="www.college1.com")[0]
        slug = college.slug
        response = self.client.get('http://127.0.0.1:8000/rightchoice/college/searchResults/'+slug+'/')
        self.assertEqual(response.status_code, 200)
    
    def test__apprent_search_results(self):
        """Apprent Search page loads"""
        response = self.client.get('http://127.0.0.1:8000/rightchoice/apprenticeships/searchResults/')
        self.assertEqual(response.status_code, 200)

    
    def test_course_uni_slug_loads(self):
        """Uni course slug page loads"""
        response = self.client.get('http://127.0.0.1:8000/rightchoice/uniCourse/1glasgow-university/')
        self.assertEqual(response.status_code, 200)
    
    def test_course_college_slug_loads(self):
        """College course slug page loads"""
        response = self.client.get('http://127.0.0.1:8000/rightchoice/collegeCourse/1city-of-glasgow-college/')
        self.assertEqual(response.status_code, 200)
    
    def test_course_app_slug_loads(self):
        """Apprent search slug page loads"""
        response = self.client.get('http://127.0.0.1:8000/rightchoice/apprenticeshipCourse/1apprenticeship-scotland/')
        self.assertEqual(response.status_code, 200)
    
    