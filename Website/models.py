from django.db import models


# Create your models here.
class Queries(models.Model):
    name = models.CharField(max_length=30)
    #contact_number = PhoneNumberField(region='IN', max_length = 10, blank = True)
    contact_number = models.IntegerField(max_length= 13)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        db_table = "queries"

    def __str__(self):
        return self.message
