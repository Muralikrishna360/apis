from django.db import models


class Ogi(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    title = models.CharField(max_length=30, default='')
    status = models.CharField(max_length=300)
    department = models.CharField(max_length=20)
    context = models.CharField(max_length=30)
    description = models.CharField(max_length=180)

    def __str__(self):
        return self.title
