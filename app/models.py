from django.db import models

class Adminlogin(models.Model):
    name=models.CharField(max_length=30)
    pas=models.CharField(max_length=30)