from django.db import models

# Create your models here.
class Inputs(models.Model):
   fname=models.CharField(max_length=200, blank=True, null=True)
   lname=models.CharField(max_length=100, blank=True, null=True)
   def __str__(self):
    return self.fname



class Forms(models.Model):
  Name = models.CharField(max_length=122)
  Contact = models.CharField(max_length=122)
  Length = models.CharField(max_length=122)
  Shoulder = models.CharField(max_length=122)
  Chest = models.CharField(max_length=122)
  Sleeves = models.CharField(max_length=122)
  Neck = models.CharField(max_length=122)
  Arm = models.CharField(max_length=122)
  Width = models.CharField(max_length=122)
  Sleevehole = models.CharField(max_length=122)
  Hip = models.CharField(max_length=122)
  Breast = models.CharField(max_length=122)
  Quantity = models.CharField(max_length=122)
  Lengthp = models.CharField(max_length=122)
  Hipp = models.CharField(max_length=122)
  Waist = models.CharField(max_length=122)
  Bottom = models.CharField(max_length=122)
  Knees = models.CharField(max_length=122)
  Calf = models.CharField(max_length=122)
  quantity = models.CharField(max_length=122)
  extra = models.CharField(max_length=122)

  def __str__(self):
    return self.Name






















