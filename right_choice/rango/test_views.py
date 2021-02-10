from django.test import TestCase, Client


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
