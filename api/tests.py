from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core import tests


class TroubleTestCase(APITestCase):
    EXPECTED_TROUBLE = {
        'code': tests.TroubleTestCase.TROUBLE_CODE,
        'title': tests.TroubleTestCase.TROUBLE_TITLE,
        'original_title': tests.TroubleTestCase.TROUBLE_ORIGINAL_TITLE,
        'description': tests.TroubleTestCase.TROUBLE_DESCRIPTION,
        'system': tests.TroubleTestCase.SYSTEM_NAME,
        'symptoms': tests.TroubleTestCase.EXPECTED_SYMPTOMS,
        'causes': tests.TroubleTestCase.EXPECTED_CAUSES,
        'solutions': tests.TroubleTestCase.EXPECTED_SOLUTIONS,
    }

    NON_EXISTENT_TROUBLE_CODE = 'Z4321'

    @classmethod
    def setUpTestData(cls):
        tests.TroubleTestCase.setUpTestData()

    def test_list_troubles(self):
        url = reverse('list-troubles')
        response = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(self.EXPECTED_TROUBLE, response.data[0])

    def test_get_non_existent_trouble(self):
        url = reverse('get-trouble', args=[self.NON_EXISTENT_TROUBLE_CODE])
        response = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_get_trouble(self):
        code = tests.TroubleTestCase.TROUBLE_CODE
        url = reverse('get-trouble', args=[code])
        response = self.client.get(url, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.EXPECTED_TROUBLE, response.data)
