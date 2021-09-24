from django.db import models

# Create your models here.
class Patient(models.Model):

           first_name = models.CharField(max_length = 50)
           last_name = models.CharField(max_length = 50)
        
           mobile = models.CharField(max_length = 50)
           email = models.CharField(max_length = 50 , default = " " , editable = 'false')
           
           password = models.CharField(max_length = 50)
           
           


           
           
        
     
       