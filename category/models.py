from django.db import models

# Create your models here.
class District(models.Model):    
    district = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.district
    
class Subdictrict(models.Model):
    subdictrict = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.subdictrict
    
class Gender(models.Model):
    gender = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.gender
    
class Living_Con(models.Model):
    living = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.living

class Career(models.Model):
    career = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.career
    
class Level_of_Education(models.Model):
    level = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.level
    
class Filed(models.Model):
    filed = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.filed
    
class AgeRange(models.Model):
    ageRange = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.ageRange


    