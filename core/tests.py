from django.test import TestCase
from core.models import Cause, Solution, Symptom, System, Trouble


class TroubleTestCase(TestCase):
    SYSTEM_NAME = "System"

    TROUBLE_CODE = "A1234"
    TROUBLE_TITLE = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
    TROUBLE_ORIGINAL_TITLE = "Donec ultrices, lacus eu porttitor venenatis"
    TROUBLE_DESCRIPTION = "Sed pretium massa nisi, eget pulvinar lectus bibendum."

    FIRST_SYMPTOM = "Interdum et malesuada fames ac."
    SECOND_SYMPTOM = "Maecenas at mollis mauris."
    EXPECTED_SYMPTOMS = [FIRST_SYMPTOM, SECOND_SYMPTOM]

    FIRST_CAUSE = "Cras placerat est vitae leo tristique."
    SECOND_CAUSE = "Morbi id nisl id nunc vulputate."
    THIRD_CAUSE = "Proin rhoncus eros et eros."
    EXPECTED_CAUSES = [FIRST_CAUSE, SECOND_CAUSE, THIRD_CAUSE]

    FIRST_SOLUTION = "Donec vitae felis felis."
    SECOND_SOLUTION = "Pellentesque non eleifend lorem."
    EXPECTED_SOLUTIONS = [FIRST_SOLUTION, SECOND_SOLUTION]

    @classmethod
    def setUpTestData(cls):
        system = System.objects.create(name=cls.SYSTEM_NAME)

        trouble = Trouble.objects.create(
            code=cls.TROUBLE_CODE,
            title=cls.TROUBLE_TITLE,
            original_title=cls.TROUBLE_ORIGINAL_TITLE,
            description=cls.TROUBLE_DESCRIPTION,
            system=system
        )

        Symptom.objects.create(description=cls.FIRST_SYMPTOM, trouble=trouble)
        Symptom.objects.create(description=cls.SECOND_SYMPTOM, trouble=trouble)

        Cause.objects.create(description=cls.FIRST_CAUSE, trouble=trouble)
        Cause.objects.create(description=cls.SECOND_CAUSE, trouble=trouble)
        Cause.objects.create(description=cls.THIRD_CAUSE, trouble=trouble)

        Solution.objects.create(description=cls.FIRST_SOLUTION, trouble=trouble)
        Solution.objects.create(description=cls.SECOND_SOLUTION, trouble=trouble)

    def test_trouble_representation(self):
        trouble = Trouble.objects.get(code=self.TROUBLE_CODE)
        assert self.TROUBLE_CODE == str(trouble)

    def test_get_trouble(self):
        trouble1 = Trouble.objects.get(code=self.TROUBLE_CODE)
        trouble2 = Trouble.get_trouble(code=self.TROUBLE_CODE)
        assert trouble1 == trouble2

    def test_get_system_name(self):
        trouble = Trouble.objects.get(code=self.TROUBLE_CODE)
        assert self.SYSTEM_NAME == trouble.get_system_name()

    def test_list_symptoms(self):
        trouble = Trouble.objects.get(code=self.TROUBLE_CODE)
        symptoms = trouble.list_symptoms()
        assert self.EXPECTED_SYMPTOMS == symptoms

    def test_list_causes(self):
        trouble = Trouble.objects.get(code=self.TROUBLE_CODE)
        causes = trouble.list_causes()
        assert self.EXPECTED_CAUSES == causes

    def test_list_solutions(self):
        trouble = Trouble.objects.get(code=self.TROUBLE_CODE)
        solutions = trouble.list_solutions()
        assert self.EXPECTED_SOLUTIONS == solutions
