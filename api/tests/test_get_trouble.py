from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import Trouble

class GetTroubleTestCase(APITestCase):
    NON_EXISTENT_TROUBLE_CODE = 'Z4321'
    EXISTENT_TROUBLE_CODE = 'A1234'

    fixtures = ['api/tests/fixtures.json']

    def test_get_non_existent_trouble(self):
        url = reverse('get-trouble', args=[self.NON_EXISTENT_TROUBLE_CODE])
        response = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_get_simple_trouble(self):
        url = reverse('get-trouble', args=[self.EXISTENT_TROUBLE_CODE])
        data = {'mode': 'simple'}
        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        trouble = Trouble.objects.get(code=self.EXISTENT_TROUBLE_CODE)
        expected_trouble = {
            'code': trouble.code,
            'title': trouble.title,
            'original_title': trouble.original_title,
            'description': trouble.description,
            'system': trouble.get_system_name()
        }

        self.assertEqual(expected_trouble, response.data)

    def test_get_extended_trouble(self):
        url = reverse('get-trouble', args=[self.EXISTENT_TROUBLE_CODE])
        data = {'mode': 'extended'}
        response = self.client.get(url, data=data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        trouble = Trouble.objects.get(code=self.EXISTENT_TROUBLE_CODE)
        expected_trouble = {
            'code': trouble.code,
            'title': trouble.title,
            'original_title': trouble.original_title,
            'description': trouble.description,
            'system': trouble.get_system_name(),
            'symptoms': trouble.list_symptoms(),
            'causes': trouble.list_causes(),
            'solutions': trouble.list_solutions()
        }

        self.assertEqual(expected_trouble, response.data)
