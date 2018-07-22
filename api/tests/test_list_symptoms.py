from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import Trouble

class ListSymptomsTestCase(APITestCase):
    NON_EXISTENT_TROUBLE_CODE = 'Z4321'
    EXISTENT_TROUBLE_CODE = 'A1234'

    fixtures = ['api/tests/fixtures.json']

    def test_with_non_existent_trouble(self):
        url = reverse('list-symptoms', args=[self.NON_EXISTENT_TROUBLE_CODE])
        response = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_with_existent_trouble(self):
        url = reverse('list-symptoms', args=[self.EXISTENT_TROUBLE_CODE])
        response = self.client.get(url, format='json')
        trouble = Trouble.objects.get(code=self.EXISTENT_TROUBLE_CODE)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(trouble.list_symptoms(), response.data)
