from django.db import models

# Create your models here.
class members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    employee_id = models.IntegerField()
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.position} {self.employee_id}"
    