from django.db import models

# Create your models here.
class StudentRecord(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    contact=models.IntegerField()
    city=models.CharField(max_length=200)


    def __str__(self):
        return self.name