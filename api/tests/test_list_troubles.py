from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import Trouble

class ListTroublesTestCase(APITestCase):
    fixtures = ['api/tests/fixtures.json']

    def setUp(self):
        self.troubles_count = Trouble.objects.count()

    def test_pagination(self):
        url = reverse('list-troubles')
        data = {'page': 1, 'size': self.troubles_count}

        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.troubles_count, response.data['count'])
        self.assertIsNone(response.data['previous'])
        self.assertIsNone(response.data['next'])
        self.assertEqual(self.troubles_count, len(response.data['results']))

    def test_two_pages_pagination(self):
        url = reverse('list-troubles')
        size = round(self.troubles_count / 2)

        data = {'page': 1, 'size': size}
        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.troubles_count, response.data['count'])
        self.assertIsNone(response.data['previous'])
        self.assertIsNotNone(response.data['next'])
        self.assertEqual(size, len(response.data['results']))

        data = {'page': 2, 'size': size}
        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.troubles_count, response.data['count'])
        self.assertIsNotNone(response.data['previous'])
        self.assertIsNone(response.data['next'])
        self.assertTrue(size >= len(response.data['results']))

    def test_simple_mode(self):
        url = reverse('list-troubles')
        data = {'page': 1, 'size': 3, 'mode': 'simple'}

        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        for result in response.data['results']:
            trouble = Trouble.objects.get(code=result['code'])

            expected_result = {
                'code': trouble.code,
                'title': trouble.title,
                'original_title': trouble.original_title,
                'description': trouble.description,
                'system': trouble.get_system_name()
            }

            self.assertEqual(expected_result, result)

    def test_extended_mode(self):
        url = reverse('list-troubles')
        data = {'page': 1, 'size': 3, 'mode': 'extended'}

        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        for result in response.data['results']:
            trouble = Trouble.objects.get(code=result['code'])

            expected_result = {
                'code': trouble.code,
                'title': trouble.title,
                'original_title': trouble.original_title,
                'description': trouble.description,
                'system': trouble.get_system_name(),
                'symptoms': trouble.list_symptoms(),
                'causes': trouble.list_causes(),
                'solutions': trouble.list_solutions()
            }

            self.assertEqual(expected_result, result)

    def test_ordering(self):
        url = reverse('list-troubles')
        data = {'page': 1, 'size': self.troubles_count, 'order': 'code'}
        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        codes = [result['code'] for result in response.data['results']]
        self.assertEqual(sorted(codes), codes)

        data = {'page': 1, 'size': self.troubles_count, 'order': '-code'}
        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        codes = [result['code'] for result in response.data['results']]
        self.assertEqual(sorted(codes, reverse=True), codes)
