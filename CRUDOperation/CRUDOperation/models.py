from django.db import models

class EmpModel(models.Model):
    empname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    salary = models.IntegerField()
    gender = models.CharField(max_length=1)
    class Meta:
        db_table = "employee"
        
    