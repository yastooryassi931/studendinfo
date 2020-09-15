from django.db import models


class UserProfile(models.Model):
    picture = models.ImageField(upload_to='pics', null=True)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    contact = models.IntegerField()
    matricnumber = models.IntegerField()
    internumber = models.IntegerField()
    bachelorcgpa = models.FloatField()
