from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ln = models.CharField(max_length=100)
    ln = models.CharField(max_length=100)

class Weight(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    date_added = models.DateField(auto_now_add= True, blank=True, null=True)
    week = models.IntegerField(blank=True, null=True)
    total_loss = models.IntegerField(blank=True, null=True)
    week_loss = models.IntegerField(blank=True, null=True)
    is_loss = models.IntegerField(blank=True, null=True)
    ave_loss = models.FloatField(blank=True, null=True)



