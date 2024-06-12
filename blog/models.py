from email.policy import default
from random import choices
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.db import models
from category.models import District,Subdictrict,Gender,Level_of_Education,Living_Con,Career,Filed,AgeRange
from multiselectfield import MultiSelectField



# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    nationalID  = models.CharField(max_length=255)
    address = models.TextField()
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    subdictrict = models.ForeignKey(Subdictrict,on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)         
    age  = models.CharField(max_length=255)
    phonenumber  = models.CharField(max_length=255)
    email  = models.CharField(max_length=255)
    living = models.ForeignKey(Living_Con,on_delete=models.CASCADE)
    level = models.ForeignKey(Level_of_Education,on_delete=models.CASCADE)
    career = models.ForeignKey(Career,on_delete=models.CASCADE)
    filed = models.ForeignKey(Filed,on_delete=models.CASCADE)
    ageRange = models.ForeignKey(AgeRange,on_delete=models.CASCADE)
    relationship = models.CharField(max_length=255)
    date = models.DateField(null = True)    
    
    
    
    
    

    
    

    

   