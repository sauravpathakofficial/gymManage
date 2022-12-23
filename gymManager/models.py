from django.db import models

class GymMembership(models.Model):      
    membership=models.CharField(max_length=15, blank=True, null=True, editable=True)
    instructor = models.CharField(max_length=50, blank=True, null=True, editable=True)
    time=models.CharField(max_length=10, blank=True, null=True, editable=True)
    capacity = models.IntegerField()

class GymMember(models.Model):
    name = models.CharField(max_length=50 ,blank=True, null=True, editable=True)
    email= models.EmailField(max_length=40, blank=True, null=True, editable=True)
    phone=models.IntegerField()
    membership = models.ForeignKey(GymMembership, on_delete=models.CASCADE)
