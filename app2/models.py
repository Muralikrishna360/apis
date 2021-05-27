from django.db import models

# Create your models here.
class Send(models.Model):
    fbuser = models.CharField(max_length=20)
    feedback = models.CharField(max_length=150)

    def __str__(self):
        return self.fbuser