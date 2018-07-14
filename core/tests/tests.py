from django.test import TestCase
from core.models import Cause, Solution, Symptom, System, Trouble

class TroubleTestCase(TestCase):
    fixtures = ['core/tests/fixtures.json']

    def setUp(self):
        self.trouble = Trouble.objects.first()

        symptoms = Symptom.objects.filter(trouble=self.trouble)
        self.EXPECTED_SYMPTOMS = sorted(symptoms.values_list('description', flat=True))

        causes = Cause.objects.filter(trouble=self.trouble)
        self.EXPECTED_CAUSES = sorted(causes.values_list('description', flat=True))

        solutions = Solution.objects.filter(trouble=self.trouble)
        self.EXPECTED_SOLUTIONS = sorted(solutions.values_list('description', flat=True))

    def test_trouble_representation(self):
        assert self.trouble.code == str(self.trouble)

    def test_get_trouble(self):
        trouble1 = Trouble.objects.get(code=self.trouble.code)
        trouble2 = Trouble.get_trouble(code=self.trouble.code)
        assert trouble1 == trouble2

    def test_get_system_name(self):
        system = self.trouble.system
        assert system.name == self.trouble.get_system_name()

    def test_list_symptoms(self):
        symptoms = self.trouble.list_symptoms()
        assert self.EXPECTED_SYMPTOMS == symptoms

    def test_list_causes(self):
        causes = self.trouble.list_causes()
        assert self.EXPECTED_CAUSES == causes

    def test_list_solutions(self):
        solutions = self.trouble.list_solutions()
        assert self.EXPECTED_SOLUTIONS == solutions
