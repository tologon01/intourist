from django.http import response
from django.test import TestCase
from django.urls import reverse
from django.db.models.query import QuerySet
from points.models import Points

class PointsListTestCase(TestCase):
    def test_open_list_success(self):
        url = reverse('points-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        points = response.context.get('points')
        self.assertIsInstance(points, QuerySet)
        

class PointsCreateTestCase(TestCase):
    def test_create_points_success(self):
        url = reverse('create-points')
        data = {
            'name': 'Issyk-Kul',
            'Location': 'Kara-Kol region',
            'description': 'Lake in KG'
        }
        response = self.client.post(url, data)
        points = Points.objects.last()
        self.assertEqual(points.name, 'Issyk-Kul')