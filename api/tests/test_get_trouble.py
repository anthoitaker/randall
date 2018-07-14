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

    def test_get_trouble(self):
        url = reverse('get-trouble', args=[self.EXISTENT_TROUBLE_CODE])
        response = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        trouble = Trouble.objects.get(code=self.EXISTENT_TROUBLE_CODE)
        self.assertEqual(trouble.title, response.data['title'])
        self.assertEqual(trouble.original_title, response.data['original_title'])
        self.assertEqual(trouble.description, response.data['description'])
        self.assertEqual(trouble.get_system_name(), response.data['system'])
