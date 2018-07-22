from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import System, Trouble

class ListSystemsTestCase(APITestCase):
    fixtures = ['api/tests/fixtures.json']

    def setUp(self):
        self.systems_count = System.objects.count()

    def test_pagination(self):
        url = reverse('list-systems')
        data = {'page': 1, 'size': self.systems_count}

        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.systems_count, response.data['count'])
        self.assertIsNone(response.data['previous'])
        self.assertIsNone(response.data['next'])
        self.assertEqual(self.systems_count, len(response.data['results']))

    def test_two_pages_pagination(self):
        url = reverse('list-systems')
        size = round(self.systems_count / 2)

        data = {'page': 1, 'size': size}
        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.systems_count, response.data['count'])
        self.assertIsNone(response.data['previous'])
        self.assertIsNotNone(response.data['next'])
        self.assertEqual(size, len(response.data['results']))

        data = {'page': 2, 'size': size}
        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.systems_count, response.data['count'])
        self.assertIsNotNone(response.data['previous'])
        self.assertIsNone(response.data['next'])
        self.assertTrue(size >= len(response.data['results']))

    def test_systems_values(self):
        url = reverse('list-systems')
        data = {'page': 1, 'size': 3}

        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        for result in response.data['results']:
            system = System.objects.get(name=result['name'])
            troubles = Trouble.objects.all()
            troubles = troubles.filter(system__name=system.name)
            troubles_count = troubles.count()

            expected_result = {
                'name': system.name,
                'troubles': troubles_count,
            }

            self.assertEqual(expected_result, result)

    def test_ordering(self):
        url = reverse('list-systems')
        data = {'page': 1, 'size': self.systems_count, 'order': 'name'}
        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        names = [result['name'] for result in response.data['results']]
        self.assertEqual(sorted(names), names)

        data = {'page': 1, 'size': self.systems_count, 'order': '-name'}
        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        names = [result['name'] for result in response.data['results']]
        self.assertEqual(sorted(names, reverse=True), names)
