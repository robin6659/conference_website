from django.db import models

# Create your models here.
class Queries(models.Model):
    name = models.CharField(max_length=30)
    contact_number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.message