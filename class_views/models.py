from django.db import models

# Create your models here.

# creating a database table/model
class Tutor(models.Model):
    first_name  = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    
    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)