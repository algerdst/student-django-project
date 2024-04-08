from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название проекта')
    image=models.ImageField(upload_to='project_images')
    slug = models.SlugField(default='')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name