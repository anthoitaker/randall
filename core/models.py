from django.db import models
from scraper.scraper.utils import import_trouble


class BaseModel(models.Model):
    created_at = models.DateTimeField('Creation Date', auto_now_add=True)
    updated_at = models.DateTimeField('Last Update', auto_now=True)

    class Meta:
        abstract = True


class System(BaseModel):
    name = models.CharField('Name', unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'system'
        verbose_name_plural = 'systems'
        ordering = ['name']


class Trouble(BaseModel):
    code = models.CharField('Code', unique=True, max_length=5)
    title = models.CharField('Title', max_length=200)
    original_title = models.CharField('Original Title', max_length=200)
    description = models.TextField('Description')
    system = models.ForeignKey(System, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'trouble'
        verbose_name_plural = 'troubles'
        ordering = ['code']

    @classmethod
    def get_trouble(cls, code):
        found = cls.objects.filter(code=code).exists()

        if not found:
            import_trouble(code)

        return cls.objects.get(code=code)

    def get_system_name(self):
        return self.system.name if self.system else None

    def list_symptoms(self):
        symptoms = Symptom.objects.filter(trouble=self.id)
        return symptoms.values_list('description', flat=True)

    def list_causes(self):
        causes = Cause.objects.filter(trouble=self.id)
        return causes.values_list('description', flat=True)

    def list_solutions(self):
        solutions = Solution.objects.filter(trouble=self.id)
        return solutions.values_list('description', flat=True)

class Symptom(BaseModel):
    description = models.TextField('Description')
    trouble = models.ForeignKey(Trouble, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'symptom'
        verbose_name_plural = 'symptoms'
        ordering = ['description']


class Cause(BaseModel):
    description = models.TextField('Description')
    trouble = models.ForeignKey(Trouble, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'cause'
        verbose_name_plural = 'causes'
        ordering = ['description']


class Solution(BaseModel):
    description = models.TextField('Description')
    trouble = models.ForeignKey(Trouble, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'solution'
        verbose_name_plural = 'solutions'
        ordering = ['description']
