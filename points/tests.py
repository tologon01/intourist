from django.http import response
from django.test import TestCase
from django.urls import reverse
from django.db.models import QuerySet
from points.models import Points
from .factories import PointsFactory


class PointsListTestCase(TestCase):
    def test_open_list_success(self):
        point_1 = PointsFactory(name='Cool place', description='Visit any time')
        point_2 = PointsFactory()

        url = reverse('points-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        points = response.context.get('points')
        self.assertIsInstance(points, QuerySet)

        self.assertEqual('Location - 1', points[1].location)
        self.assertEqual(points[0].description, 'Visit any time')

class PointsCreateTestCase(TestCase):
    def test_create_place_success(self):
        url = reverse('create-points')
        data = {
            'name': "Issyk-Kul",
            'location': "Kara-Kol region",
            'description': "Lake in KG"
        }
        response = self.client.post(url, data)
        points = Points.objects.last()
        self.assertEqual(points.name, "Issyk-Kul")