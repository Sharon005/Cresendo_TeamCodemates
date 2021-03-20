from django.db import models

# Create your models here.
class Inputs(models.Model):
   fname=models.CharField(max_length=200, blank=True, null=True)
   lname=models.CharField(max_length=100, blank=True, null=True)
   def __str__(self):
    return self.name

'''class KurtaMeasurements(models.Model):
  nname=models.FloatField(max_length=100)
  sname=models.FloatField(max_length=100)
  aname=models.FloatField(max_length=50)
  cname=models.FloatField(max_length=100)
  bname=models.FloatField(max_length=100)
  stname=models.FloatField(max_length=100)
  wname=models.FloatField(max_length=50)
  hname=models.FloatField(max_length=100)
  shname=models.FloatField(max_length=30)
  wrname=models.FloatField(max_length=10)
  ahname=models.FloatField(max_length=30)
  def __str__(self):
    return self.name
  

class PyjamaMeasurements(models.Model):
  lename=models.FloatField(max_length=100)
  hiname=models.FloatField(max_length=50)
  waname=models.FloatField(max_length=50)
  boname=models.FloatField(max_length=100)
  kname=models.FloatField(max_length=30)
  caname=models.FloatField(max_length=30)
  def __str__(self):
    return self.name'''