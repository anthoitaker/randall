from django.db import models


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
    system = models.ForeignKey(System, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'trouble'
        verbose_name_plural = 'troubles'
        ordering = ['code']


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
